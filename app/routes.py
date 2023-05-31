from app import app
from flask import render_template, request, redirect, url_for
from .models.base import Session
from .models.model import Products, Customers

session = Session()
@app.route('/', strict_slashes=False)
def index():
    #prods = Products.query.all()
    prods = session.query(Products).all()
    return render_template('index.html', prods=prods)

@app.route('/sign_in_register', methods=['GET', 'POST'])
def sign_in():
    message = ""
    #user_name = ""
    if request.form:
        if request.method == "POST":
            if request.args.get('name') == 'signup':
                customer_email = request.form.get('mobile_or_email')
                check_user = session.query(Customers).filter_by(customer_email=customer_email).first()
                if check_user:
                    error="email already exists"
                    return redirect(url_for('sign_in', error=error))
                user = Customers(customer_name=request.form.get('fullname'), customer_email=request.form.get('mobile_or_email'), customer_pass=request.form.get('password'))
                session.add(user)
                session.commit()
                message = "Your account has been created successfully"
            else:
                customer_email=request.form.get('username')
                customer_pass=request.form.get('password')
                user=session.query(Customers).filter_by(customer_email=customer_email).first()
                if not user:
                    error="Invalid login details"
                    return redirect(url_for('sign_in', error=error))
                user_name=str(user).split(' ')
                first_name=user_name[0]
                return redirect(url_for('index', user_name=first_name))
    return render_template('sign_in_register.html', message=message)

@app.route('/cart')
def cart_page():
    return render_template("cart.html")

@app.route('/prod/<name>', methods=['GET','POST'])
def get_product(name):
    #prod_name = request.args.get('name')
    get_prod = session.query(Products).filter_by(product_name=name).first()
    #return("{}".format(get_prod[product_price]))
    return render_template("product_page.html", prod_name=name, get_prod=get_prod)
