#!/usr/bin/python3
'''module for defining the flask routes'''
import bcrypt
from app import app
from flask import render_template, request, redirect, url_for, session, jsonify
from .models.base import DBSession
from .models.model import Products, Customers, Cartitems, Shippings
import math

db_session = DBSession()
@app.route('/', strict_slashes=False)
def index():
    '''defining the index page'''
    #prods = Products.query.all()
    prods = db_session.query(Products).all()
    return render_template('index.html', prods=prods)

@app.route('/sign_in_register', methods=['GET', 'POST'])
def sign_in():
    '''defining login and register functionality'''
    message = ""
    #user_name = ""
    '''check if a form is rwceived'''
    if request.form:
        # check id form inpirs were submitted
        if request.method == "POST":
            # check if it is a signup
            if request.args.get('name') == 'signup':
                customer_email = request.form.get('mobile_or_email')
                # check if a customer already exiats with that email
                check_user = db_session.query(Customers).filter_by(customer_email=customer_email).first()
                if check_user:
                    error="email already exists"
                    return redirect(url_for('sign_in', error=error))
                # continue if customer does not already exist
                customer_password = request.form.get('password')
                customer_bytes = customer_password.encode('utf-8')
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(customer_bytes, salt)
                user = Customers(customer_name=request.form.get('fullname'), customer_email=request.form.get('mobile_or_email'), customer_pass = hashed_password)
                db_session.add(user)
                db_session.commit()
                message = "Your account has been created successfully"
                # if it was a sign in form that was submitted
            else:
                customer_email=request.form.get('username')
                customer_pass=request.form.get('pass')
                if customer_email == "" or customer_pass == "":
                    error="Sorry, invalid credentials"
                    return redirect(url_for('sign_in', error=error))
                user_bytes  = customer_pass.encode('utf-8')
                user=db_session.query(Customers).filter_by(customer_email=customer_email).first()
                if not user:
                    error="Sorry, email not recognized"
                    return redirect(url_for('sign_in', error=error))
                hashed_pass = user.customer_pass.encode('utf-8')
                if not bcrypt.checkpw(user_bytes, hashed_pass):
                    error="Incorrect password"
                    return redirect(url_for('sign_in', error=error))
                else:
                    session['user_id'] = user.customer_id
                    session['username'] = user.customer_name
                    #user_name=str(user).split(' ')
                    user_name = user.customer_name.split(' ')
                    first_name = user_name[0]
                    session['first_name'] = first_name
                    return redirect(url_for('index', user_name=session['username'], user_id=session['user_id']))
    return render_template('sign_in_register.html', message=message)

@app.route('/sign_out')
def log_out():
    '''define a log out'''
    if session['user_id']:
        session.pop('user_id', None)
        session.pop('username', None)
        session.pop('first_name', None)
        return redirect(url_for('sign_in'))
    return redirect(url_for('index'))

def subTotal():
    '''get total from cartitems table'''
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
    '''render the cart page'''
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
        error=""
        '''shipping_address = request.form['shipAdd']
        shipping_city = request.form['shipCity']
        shipping_state = request.form['shipState']
        shipping_country = request.form['shipCountry']
        shipping_phone = request.form['shipPhone']
        shipping_zip = request.form['shipZip']'''
        if shipping_address == "" or shipping_city == "" or shipping_state == "" or shipping_country == "" or shipping_phone == "" or shipping_zip == "":
            error = "Sorry, all fields are required"
            return redirect(url_for('cart_page', error=error))
        '''if len(shipping_phone) is not 11:
            error = "Phone number must be 11 digits"
            return redirect(url_for('ca
rt_page', error=error))'''
        ship_item = Shippings(shipping_customer_id=shipping_id, shipping_address=shipping_address, shipping_city=shipping_city, shipping_state=shipping_state, shipping_country=shipping_country, shipping_phone=shipping_phone, shipping_zip=shipping_zip, shipping_amount=720)
        db_session.add(ship_item)
        db_session.commit()
        my_total = subTotal()
        shipping_details = db_session.query(Shippings).filter_by(shipping_customer_id=shipping_id).first()
        #return jsonify({'my_total' : my_total})
        #return shipping_details
        return render_template("checkout.html", shipping_details=shipping_details, my_total=my_total)
    return render_template("checkout.html")

@app.route('/modify_cart/<p_id>', methods=['GET', 'POST'])
def remove_item(p_id):
    check_item = db_session.query(Cartitems).filter_by(cart_product_id=p_id, cart_customer_id=session['user_id']).first()
    db_session.delete(check_item)
    db_session.commit()
    #return render_template("cart.html")
    return redirect(url_for('cart_page'))

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.teardown_request
def teardownRequest(exception):
    if exception:
        db_session.rollback()
    db_session.close()

@app.route('/buyit')
def landing_page():
    return render_template("buyit.html")
