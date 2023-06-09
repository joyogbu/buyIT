#!/usr/bin/python3
from app import app
from flask import render_template, request, redirect, url_for, session
from .models.base import DBSession
from .models.model import Products, Customers, Cartitems, Shippings
import math

db_session = DBSession()
@app.route('/', strict_slashes=False)
def index():
    #prods = Products.query.all()
    prods = db_session.query(Products).all()
    return render_template('index.html', prods=prods)

@app.route('/sign_in_register', methods=['GET', 'POST'])
def sign_in():
    message = ""
    #user_name = ""
    if request.form:
        if request.method == "POST":
            if request.args.get('name') == 'signup':
                customer_email = request.form.get('mobile_or_email')
                check_user = db_session.query(Customers).filter_by(customer_email=customer_email).first()
                if check_user:
                    error="email already exists"
                return redirect(url_for('sign_in', error=error))
                user = Customers(customer_name=request.form.get('fullname'), customer_email=request.form.get('mobile_or_email'), customer_pass=request.form.get('password'))
                db_session.add(user)
                db_session.commit()
                message = "Your account has been created successfully"
            else:
                customer_email=request.form.get('username')
                customer_pass=request.form.get('password')
                user=db_session.query(Customers).filter_by(customer_email=customer_email).first()
                if not user:
                    error="Invalid login details"
                    return redirect(url_for('sign_in', error=error))
                session['user_id'] = user.customer_id
                session['username'] = user.customer_name
                #user_name=str(user).split(' ')
                user_name = user.customer_name.split(' ')
                first_name=user_name[0]
                return redirect(url_for('index', user_name=session['username'], user_id=session['user_id']))
    return render_template('sign_in_register.html', message=message)

@app.route('/sign_out')
def log_out():
    if session['user_id']:
        session.pop('user_id', None)
        session.pop('username', None)
        return redirect(url_for('sign_in'))
    return redirect(url_for('index'))

def subTotal():
    sub_total=0
    all_items = db_session.query(Cartitems).filter_by(cart_customer_id=session['user_id']).all()
    #sub_total = all_items.cart_quantity * all_items.item.product_price
    my_sum=[]
    for things in all_items:
        total=things.cart_quantity * things.item.product_price
        my_sum.append(total)
        sub_total = sum(my_sum) 
    return (sub_total)

@app.route('/cart', methods=['GET', 'POST'])
@app.route('/cart/<int:id>', methods=['GET', 'POST'])
def cart_page(id=None):
    #cart_item = None
    quantity = 0
    sub_total = 0
    '''check if a product is selected and a customer is logged in '''
    #if id:
    if id and 'user_id' in session:
        #cart_item = ""
        if request.form.get('prod_qty') is not None:
            quantity = int(request.form.get('prod_qty'))
        get_product = db_session.query(Products).filter_by(product_id=id).first()
        check_product = db_session.query(Cartitems).filter_by(cart_product_id=id, cart_customer_id=session['user_id']).first()
        if check_product:
            check_product.cart_quantity = check_product.cart_quantity + quantity
            db_session.commit()
        else:
            cart_item = Cartitems(cart_product_id=id, cart_customer_id = session['user_id'], cart_quantity=quantity)
            db_session.add(cart_item)
            db_session.commit()
        all_items = db_session.query(Cartitems).filter_by(cart_customer_id=session['user_id']).all()
        #sub_total = all_items.cart_quantity * all_items.item.product_price
        return render_template("cart.html", quantity=quantity, all_items=all_items, sub_total=subTotal())
    else:
        if 'user_id' in session:
            all_items = db_session.query(Cartitems).filter_by(cart_customer_id=session['user_id']).all()
            return render_template("cart.html", all_items=all_items, sub_total=subTotal())
        return render_template("cart.html")

@app.route('/prod/<name>', methods=['GET','POST'])
def get_product(name):
    #prod_name = request.args.get('name')
    get_prod = db_session.query(Products).filter_by(product_name=name).first()
    #return("{}".format(get_prod[product_price]))
    return render_template("product_page.html", prod_name=name, get_prod=get_prod)

@app.route('/buy/checkout', methods=['POST', 'GET'])
def check_out():
    if request.method == "POST":
        shipping_id = session['user_id']
        shipping_address = request.form.get('shipping_address')
        shipping_city = request.form.get('shipping_city')
        shipping_state = request.form.get('shipping_state')
        shipping_country = request.form.get('shipping_country')
        shipping_phone = request.form.get('phone')
        shipping_zip = request.form.get('zip_code')
        ship_item = Shippings(shipping_customer_id=shipping_id, shipping_address=shipping_address, shipping_city=shipping_city, shipping_state=shipping_state, shipping_country=shipping_country, shipping_phone=shipping_phone, shipping_zip=shipping_zip, shipping_amount=720)
        db_session.add(ship_item)
        db_session.commit()
    my_total = subTotal()
    shipping_details = db_session.query(Shippings).filter_by(shipping_customer_id=shipping_id).first()
    return render_template("checkout.html", shipping_details=shipping_details, my_total=my_total)
    #return render_template("checkout.html")

@app.route('/modify_cart/<p_id>', methods=['GET', 'POST'])
def remove_item(p_id):
    check_item = db_session.query(Cartitems).filter_by(cart_product_id=p_id, cart_customer_id=session['user_id']).first()
    db_session.delete(check_item)
    db_session.commit()
    #return render_template("cart.html")
    return redirect(url_for('cart_page'))

@app.route('/buyit')
def landing_page():
    return render_template("buyit.html")
