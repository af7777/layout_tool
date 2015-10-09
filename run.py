#!/usr/bin/python2
# -*- coding: utf-8 -*-

import data_import
import template_storage
import grid_layout
import frame_layout
import page_layout
import fonts
import os



page_size = [210,297]
pdf_dir = (os.path.join(os.getcwd(),'out/pdf'))

data = data_import.adv_text('/home/raven/git/pages/data/adv_source/horeca_1.csv')

fonts.init_fonts()

for page_number,page_offers in data.iteritems():
	template = template_storage.test(page_size)
	template = grid_layout.generic(template,page_offers)
	template = frame_layout.generic_frame(template)
	page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(page_number) + '_test_1.pdf')