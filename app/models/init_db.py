#!/usr/bin/python3

import sqlalchemy
from model import Customers, Products
from base import engine, Base, Session

Base.metadata.create_all(engine)
session = Session()

prod1 = Products("Introduction to AI by Joy O.", "This is a well structured and defined book on AI", "Books", 800)
prod2 = Products("What every man wants from a woman", "This is a book on relationship and marriage written by Steve Harvey", "Books", 900)

session.add(prod1)
session.add(prod2)

session.commit()
session.close()


