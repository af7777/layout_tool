#!/usr/bin/python2
# -*- coding: utf-8 -*-


from fonts import fonts
from data import adv_text
from data import reg_text
from templates import horeca
import grid.generic
import frame.generic
import generator.page_layout
import os
from reportlab.lib.units import mm


page_size = [210,297]
pdf_dir = (os.path.join(os.getcwd(),'out/pdf'))

offer_data = reg_text.init('/home/raven/git/pages/data/reg_source/68.csv','/home/raven/git/pages/imageDb/horeca/')

fonts.init()

for page_number,page_offers in offer_data.iteritems():
	print page_offers
	template = horeca.init(page_size)
	template = grid.generic.init(template,page_offers)
	template = frame.generic.init(template)
	generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(page_number) + '_test_1.pdf')