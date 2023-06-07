#!/usr/bin/python3

from sqlalchemy import DateTime, ForeignKey, String, Integer, Text, Numeric, Column
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from .base import Base, engine

class Customers(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(30), nullable=False)
    customer_email = Column(String(30), nullable=False)
    customer_pass = Column(String(200), nullable=False)
    date_added = Column(DateTime, default=datetime.now())
    #prods = relationship('Customers', backref='buyer')
    carts = relationship('Cartitems', backref='owner', lazy='dynamic')
    ships = relationship('Shippings', backref='shipper', lazy='dynamic')

    def __init__(self, customer_name, customer_email, customer_pass):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_pass = customer_pass
#    def __repr__(self):
 #       return "{}".format(self.customer_name)

class Products(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(30), nullable=False)
    product_desc = Column(Text(200))
    product_cat = Column(String(30))
    product_price = Column(Numeric, nullable=False)
    date_added = Column(DateTime, default=datetime.now())
    date_updated = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    cust_id = Column(Integer, ForeignKey('customers.customer_id'))
    prods = relationship('Customers', backref='buyer')
    cartss = relationship('Cartitems', backref='item', lazy='dynamic')

    def __init__(self, product_name, product_desc, product_cat, product_price):
        self.product_name = product_name
        self.product_desc = product_desc
        self.product_cat = product_cat
        self.product_price = product_price

    def __repr__(self):
        return "{}".format(self.product_name)

class Cartitems(Base):
    __tablename__ = "cartitems"
    cart_id = Column(Integer, primary_key=True)
    cart_product_id = Column(Integer, ForeignKey('products.product_id'))
    cart_customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    cart_quantity = Column(Integer())
    Cart_date_created = Column(DateTime, default=datetime.now())
    #carts = relationship('Customers', backref='cart', lazy='dynamic')

    #def __init__(self, cart_product_id, cart_customer_id):
     #   self.cart_product_id = cart_product_id
      #  self.cart_customer_id = cart_customer_id

class Shippings(Base):
    __tablename__ = "shipping"
    details_id = Column(Integer, primary_key=True)
    shipping_customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    shipping_address = Column(String(200))
    shipping_city = Column(String(100))
    shipping_state = Column(String(50))
    shipping_country = Column(String(50))
    shipping_phone = Column(String(11))
    shipping_zip = Column(String(10))
    shipping_amount = Column(Numeric, default=590)
    date_added = Column(DateTime, default=datetime.now())
    date_updated = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    def __init__(self, shipping_customer_id, shipping_address, shipping_city, shipping_state, shipping_country, shipping_phone, shipping_zip, shipping_amount):
        self.shipping_customer_id = shipping_customer_id
        self.shipping_address = shipping_address
        self.shipping_city = shipping_city
        self.shipping_state = shipping_state
        self.shipping_country = shipping_country
        self.shipping_phone = shipping_phone
        self.shipping_zip = shipping_zip
        self.shipping_amount =shipping_amount
