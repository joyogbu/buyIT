#!/usr/bin/python3

import sqlalchemy
from model import Customers, Products
from base import engine, Base, DBSession

Base.metadata.create_all(engine)
db_session = DBSession()

prod1 = Products("Introduction to AI by Joy O.", "This is a well structured and defined book on AI", "Books", 800)
prod2 = Products("What every man wants from a woman", "This is a book on relationship and marriage written by Steve Harvey", "Books", 900)

db_session.add(prod1)
db_session.add(prod2)

db_session.commit()
db_session.close()


