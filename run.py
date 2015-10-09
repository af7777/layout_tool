#!/usr/bin/python2
# -*- coding: utf-8 -*-


from fonts import fonts
from data import adv_text
from templates import horeca
import grid.generic
import frame.generic
import os


page_size = [210,297]
pdf_dir = (os.path.join(os.getcwd(),'out/pdf'))

offer_data = adv_text.init('/home/raven/git/pages/data/adv_source/horeca_1.csv','/home/raven/git/pages/imageDb/horeca/')

fonts.init()

for page_number,page_offers in offer_data.iteritems():
	print page_offers
	template = horeca.init(page_size)
	template = grid.generic.init(template,page_offers)
	template = frame.generic.init(template)
#	page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(page_number) + '_test_1.pdf')