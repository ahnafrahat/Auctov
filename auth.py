

from flask import Blueprint, render_template, request, redirect, url_for, flash, session


from db import create_user_table, add_user, login_user, create_product_table, create_bid_table

auth = Blueprint("auth", __name__, static_folder="static",
                 template_folder="templates")


@auth.route("/getSignup", methods=["GET"])
def getSignup():

    # create_user_table()

    # create_product_table()

    return render_template("register.html")


@auth.route("/postSignup", methods=["POST"])
def postSignup():

    print(" in post signup")

    username = request.form.get('UserName')
    email = request.form.get('Email')
    password = request.form.get('Password')

    new_user = add_user(username=username, email=email, password=password)

    if not new_user:

        return redirect(url_for('auth.getSignup'))

    else:

        return redirect(url_for('auth.getLogin'))


@auth.route("/getLogin", methods=["GET"])
def getLogin():
    return render_template("login.html")


# login a new user  if error redirects to getLog in view
@auth.route("/postLogin", methods=["POST"])
def postLogin():

    email = request.form.get('Email')
    password = request.form.get('Password')

    result = login_user(email=email, password=password)

    if not result:
        return redirect(url_for('auth.getLogin'))
    else:
        session['user_id'] = result["user_id"]
        session['UserName'] = result["username"]
        session['userEmail'] = result["useremial"]

        return redirect(url_for('index'))


@auth.route("/getLogout", methods=["GET"])
def getLogout():
    session.clear()
    return redirect(url_for('index'))
