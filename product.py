from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from decorators import is_loggedIn
from uploadUtils import photos
from datetime import datetime

from db import add_product, get_all_products, get_user_products, get_single_product

product = Blueprint("product", __name__,
                    static_folder="static", template_folder="templates")


@product.route("/getAddProduct", methods=["GET"])
@is_loggedIn
def getAddProduct():

    get_user_products(user_id=1)

    return render_template("start_selling.html")


@product.route("/postAddProduct", methods=["POSt"])
@is_loggedIn
def postAddProduct():

    now = datetime.now()
    name = now.strftime("%m%d%Y%H%M%S")
    name = name + "."

    if 'ProductImage' in request.files:
        filename = photos.save(request.files['ProductImage'], name=name)

    result = add_product(title=request.form.get('product_title'),
                         description=request.form.get('product_description'),
                         reserve_price=request.form.get('reserve_price'),
                         bin_price=request.form.get('bin_price'),
                         image=filename,
                         user_id=session['user_id'])

    return redirect(url_for('product.getAddProduct'))


@product.route("/getMarketPlace", methods=["GET"])
def getMarketPlace():

    products = get_all_products()

    return render_template("marketplace.html", products=products)


@product.route("/singleProduct/<int:product_id>", methods=["GET"])
def singleProduct(product_id):
    productId = product_id

    product = get_single_product(productId)

    return render_template("listing_details.html", product=product)
