#!/usr/bin/python2
# -*- coding: utf-8 -*-

import csv
import re
import os

'''schema = {'page':string
			'header':string
			'text':string
			'mcc art':string
			'mgb art':string
			'price':string
			'image':string
			}'''

def image_plain_folder(path):
	pool = {}
	for root,dirs,files in os.walk(path):
		for f in files:
			mgb = f[:f.find('-')]
			pool[mgb] = os.path.join(root,f)
	return pool


def adv_text(path):
	offers = {}
	image_pool = image_plain_folder('/home/raven/git/pages/imageDb/horeca/')
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
				if mgb_art not in image_pool:
					image = '/home/raven/git/pages/imageDb/test1.jpg'
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
	image_plain_folder('/home/raven/git/pages/imageDb/test/')
	#for key,value in adv_text('/home/raven/git/pages/data/adv_source/test1.csv').iteritems():
	#	print key
	#	for offer in value:
	#		print '\t',offer['mcc art']