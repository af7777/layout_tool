#!/usr/bin/python2
# -*- coding: utf-8 -*-

import csv
import re
import os
import images_plain_folder

'''schema = {'page':string
			'header':string
			'text':string
			'mcc art':string
			'mgb art':string
			'price':string
			'image':string
			}'''




def init(path,images_path):
	offers = {}
	image_pool = images_plain_folder.init(images_path)
	with open(path,'rb') as csvfile:
		reader = csv.reader(csvfile,delimiter=';',quotechar='"')
		row_number = -1
		for row in reader:
			row_number += 1
			if row_number > 7:
				header = row[9]
				text = row[10]
				mcc_art = row[1]
				mgb_art = row[0]
				price = row[12].replace('.','')[:-1].replace(',','.')
				page = row[13]
				if str(mgb_art) not in image_pool:
					image = {'text': 'place holder', 'image path': '/home/raven/git/pages/imageDb/test1.jpg', 'clipping path': False}
				else:
					image = image_pool[mgb_art]
				
				offer = {
						'page':page,
						'header':header,
						'text':text,
						'mcc art':mcc_art,
						'mgb art':mgb_art,
						'price':price,
						'image':image,
						'image override': None,
						}
				if page not in offers:
					offers[page] = [offer]
				else:
					array = offers[page]
					array.append(offer)
					offers[page] = array

	return offers 

if __name__ == '__main__':
	for key,value in init('/home/raven/git/pages/data/adv_source/horeca_1.csv','/home/raven/git/pages/imageDb/horeca/').iteritems():
		print key
		for offer in value:
			print '\t',offer['mcc art']
			print '\t\t',offer['image']