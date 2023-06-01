from app import app
from flask import render_template, request, redirect, url_for, session
from .models.base import DBSession
from .models.model import Products, Customers

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

@app.route('/cart', methods=['GET', 'POST'])
def cart_page():
    if request.method == 'POST':
        #print("not empty")
        return render_template("cart.html")
    else:
        return render_template("index.html")

@app.route('/prod/<name>', methods=['GET','POST'])
def get_product(name):
    #prod_name = request.args.get('name')
    get_prod = db_session.query(Products).filter_by(product_name=name).first()
    #return("{}".format(get_prod[product_price]))
    return render_template("product_page.html", prod_name=name, get_prod=get_prod)
