#!/usr/bin/python3

import sqlalchemy
from app import app
from app.models.model import Customers, Products, Cartitems, Shippings
from app.models.base import Base, engine, DBSession

db_session = DBSession()

def fn():
    output = "console is up"
    print (output)

def create_table():
    Base.metadata.create_all(engine, checkfirst=True)

if __name__ == '__main__':
    create_table()
