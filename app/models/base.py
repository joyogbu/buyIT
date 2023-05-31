#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://root:15AGcuVuTN@localhost/portfolio_db")
Session = sessionmaker(bind=engine)

Base = declarative_base()
#Base.query = Session.query_property()
