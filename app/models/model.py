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

    def __init__(self, customer_name, customer_email, customer_pass):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_pass = customer_pass
    def __repr__(self):
        return "{}".format(self.customer_name)

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

    def __init__(self, product_name, product_desc, product_cat, product_price):
        self.product_name = product_name
        self.product_desc = product_desc
        self.product_cat = product_cat
        self.product_price = product_price

    def __repr__(self):
        return "{}".format(self.product_name)
# Base.metadata.create_all(engine)
