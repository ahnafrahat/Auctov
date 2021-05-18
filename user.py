from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from decorators import is_loggedIn

from db import  get_user_products

user = Blueprint("user",__name__, static_folder="static", template_folder="templates")


@is_loggedIn
@user.route("/getUserProfile", methods =["GET"])
def getUserProfile():

    products = get_user_products(user_id=session['user_id'])

    return render_template("profile.html", products=products)