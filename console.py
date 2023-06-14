#!/usr/bin/python3
'''command line interpreter for managing CRUD operations'''


import cmd
import sqlalchemy
from app import app
from app.models.model import Customers, Products, Cartitems, Shippings
from app.models.base import Base, engine, DBSession
db_session = DBSession()

class Buyit(cmd.Cmd):
    '''base class'''
    prompt = '(buyit) '
    __classes = ['Products', 'Customers']

    def do_create(self, line):
        '''create a table based on the supplied argument'''
        Base.metadata.create_all(engine, tables=[Base.metadata.tables[line]], checkfirst=True)
        print (line)

    def do_add(self, line):
        '''add a new product to the product table'''
        Base.metadata.create_all(engine)
        if line == "":
            print("No argument supplied")
            return
        args = line.split('(')
        if args[0] not in Buyit.__classes:
            print("table does not exist")
            return
        arg_s = args[1].split(',')
        if len(arg_s) < 5:
            print("** You have incomplete object initialization **")
            return
        print(line)
        new_product = eval(line)
        db_session.add(new_product)
        db_session.commit()
        #db_session.close()
        print("** Product added successfully **")

    def do_quit(self, line):
        '''quit the interpreter'''
        return True

    def emptyline(selg):
        '''do nothing if no argument supplied'''
        pass

if __name__ == '__main__':
    Buyit().cmdloop()
