#!/usr/bin/python3

import cmd
import sqlalchemy
from app import app
from app.models.model import Customers, Products, Cartitems, Shippings
from app.models.base import Base, engine, DBSession
db_session = DBSession()

class Buyit(cmd.Cmd):
    prompt = '(buy) '
    __classes = ['Products', 'Customers']

    def do_create(self, line):
        Base.metadata.create_all(engine, tables=[Base.metadata.tables[line]], checkfirst=True)
        print (line)

    def do_add(self, line):
        Base.metadata.create_all(engine)
        new_product = line
        db_session.add(new_product)
        db_session.commit()
        db_session.close()

    def do_quit(self, line):
        return True

    def emptyline(selg):
        pass

if __name__ == '__main__':
    Buyit().cmdloop()
