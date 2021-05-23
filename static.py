from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from decorators import is_loggedIn
from uploadUtils import photos
from datetime import datetime


static = Blueprint("static", __name__,
                   static_folder="static", template_folder="templates")


@static.route("/about", methods=["GET"])
def about():

    return render_template("about_us.html")


@static.route("/contact", methods=["GET"])
def contact():

    return render_template("contact.html")


@static.route("/faq", methods=["GET"])
def faq():

    return render_template("faq.html")
