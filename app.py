from flask import Flask, render_template, request, redirect, Blueprint
from uploadUtils import photos

from flask_uploads import configure_uploads


from auth import auth
from product import product
from user import user

from db_config import mysql

app = Flask(__name__)
app.secret_key = "asd"

app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
configure_uploads(app, photos)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Auctov'

mysql.init_app(app)


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(product, url_prefix="/product")
app.register_blueprint(user, url_prefix="/user")


@app.route('/')
def index():

    return render_template("home.html")


if __name__ == "__main__":

    app.run(debug=True)
