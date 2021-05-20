from db_config import mysql


def create_user_table():
    cursor = mysql.connection.cursor()

    query = '''CREATE TABLE user ( \
    user_id int NOT NULL AUTO_INCREMENT, \
    username varchar(255), \
    email varchar(255), \
    password varchar(255) ,\
    PRIMARY KEY (user_id) \
    );'''

    try:
        cursor.execute(query)
        mysql.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        return False


def create_product_table():

    cursor = mysql.connection.cursor()

    query = '''CREATE TABLE product ( \
    product_id int NOT NULL AUTO_INCREMENT, \
    title varchar(255), \
    description varchar(255), \
    reserve_price int, \
    bin_price int, \
    image varchar(255) ,\
    user_id int,\
    PRIMARY KEY (product_id) \
    );'''

    try:
        cursor.execute(query)
        mysql.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        return False


def check_table_exist():

    cursor = mysql.connection.cursor()
    query = "SHOW TABLES LIKE 'user'"
    try:

        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            print("table exists")
        else:
            print("table not exists")

        cursor.close()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return False


def check_if_user_exists(email):

    cursor = mysql.connection.cursor()

    query = "SELECT * FROM user WHERE email='%s'" % (email)

    try:
        cursor.execute(query)
        user = cursor.fetchone()
        cursor.close()
        if user:
            print("user exists")

            return True
        else:
            print("user exists")
            return False

    except Exception as e:
        print(e)
        cursor.close()
        return False


def add_user(username, email, password):

    email_exists = check_if_user_exists(email)

    if email_exists:
        return False

    cursor = mysql.connection.cursor()

    query = "INSERT INTO user (username, email, password) VALUES ( %s, %s, %s)"
    value = (str(username), str(email), str(password))
    try:
        cursor.execute(query, value)
        mysql.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return False


def login_user(email, password):

    cursor = mysql.connection.cursor()

    query = "SELECT * FROM user WHERE email='%s' and password='%s'" % (
        email, password)

    try:
        cursor.execute(query,)
        user = cursor.fetchone()
        cursor.close()
        if user:

            return {
                "user_id": user[0],
                "username": user[1],
                "useremial": user[2]
            }

        else:
            return False

    except Exception as e:
        print(e)
        cursor.close()
        return False


def add_product(title, description, reserve_price, bin_price, image, user_id):
    cursor = mysql.connection.cursor()

    query = "INSERT INTO product (title, description, reserve_price, bin_price, image, user_id) VALUES ( %s, %s, %s, %s, %s, %s)"
    value = (str(title), str(description), int(reserve_price),
             int(bin_price), str(image), int(user_id))
    try:
        cursor.execute(query, value)
        mysql.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return False


def get_all_products():

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM product"

    try:
        cursor.execute(query)
        products = cursor.fetchall()
        cursor.close()

        return products
    except Exception as e:
        print(e)
        cursor.close()
        return False


def get_user_products(user_id):

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM product WHERE user_id='%s' " % (int(user_id))

    try:
        cursor.execute(query)
        products = cursor.fetchall()
        cursor.close()
        return products
    except Exception as e:
        print(e)
        cursor.close()
        return False


def get_single_product(product_id):

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM product WHERE product_id='%s' " % (int(product_id))

    try:
        cursor.execute(query)
        product = cursor.fetchone()
        cursor.close()
        return product
    except Exception as e:
        print(e)
        cursor.close()
        return False
