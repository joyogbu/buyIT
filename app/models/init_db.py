#!/usr/bin/python3

import sqlalchemy
from model import Customers, Products
from base import engine, Base, DBSession

Base.metadata.create_all(engine)
db_session = DBSession()

prod1 = Products('Geneva Unisex Casual Wrist Watch', "Jazz up your outfits and add sophistication to your look with this exquisite watch that has been specially designed for you", "Watches", 3500, "watch_1.jpg")
prod2 = Products("2 In 1 Stainless Steel Ladies Women Female Wrist Watch And Bracelet-Blue/Gold", "This new fashion rhinestone analog quartz stainless steel gold wrist watch features a round case with double row chronograph decorations , which is a timepiece you will surely love. It is perfect for everyday wear.", "Watches", 3900, "watch_2.jpg")
db_session.add(prod1)
db_session.add(prod2)

db_session.commit()
db_session.close()


