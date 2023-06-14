#!/usr/bin/python3
'''using script to add products'''

import sqlalchemy
from model import Customers, Products
from base import engine, Base, DBSession

Base.metadata.create_all(engine)
db_session = DBSession()

"""prod1 = Products('Geneva Unisex Casual Wrist Watch with bracelets', "Jazz up your outfits and add sophistication to your look with this exquisite watch that has been specially designed for you", "Watches", 3500, "watch1.jpg")
prod2 = Products("2 In 1 Stainless Steel Ladies Women Female Wrist Watch And Bracelet-Blue/Gold", "This new fashion rhinestone analog quartz stainless steel gold wrist watch features a round case with double row chronograph decorations , which is a timepiece you will surely love. It is perfect for everyday wear.", "Watches", 3900, "watch2.jpg")"""
"""
prod3 = Products('Infinix Smart 7 HD 6.6" 64GB/2GB RAM 5000mAh Android 12 Fingerprint', 'Smart 7 HDYou can take advantage of a wide range of outstanding features that complement your lifestyle with the amazing Infinix SMART 7 HD phone.', 'Phones', 55450, 'phone1.jpg')
prod4 = Products('Senwei 4.5KVA Manul Start Generator SV5200. - Low Noise Level', 'This amazing generator adopts an advanced technology in design and performance peculiar only to the Senwei Brand.', 'Generators', 120909, 'generator1.jpg')"""

prod5 = Products("Women Handbag For Women Bag Ladies Purse Crossbody Satchel - White", "Women Handbag For Women Bag Ladies Purse Crossbody Satchel - White color", "Bags", 7900, 'bag1.jpg')
prod6 = Products("ADIDAS Core / Neo Sport Shoes Vs Advantage", "These court-inspired shoes add style with stitched 3-Stripes on the outer side and perforated 3-Stripes on the inner side. adidas men's sneakers mixing comfort and style", 'Shoes', 32400, "shoe1.jpg")
db_session.add(prod5)
db_session.add(prod6)

db_session.commit()
db_session.close()


