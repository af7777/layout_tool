#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
from reportlab.lib.units import mm


import utils.image.fit_to_box
import utils.layout.working_area

def init(page_size,verbose = False,header = None,page_num = 1):
	page_width,page_height = page_size[0],page_size[1]

	template = {
		'top': 
			{	
			'type' : 'image',
			'file_name': u'/home/raven/git/pages/imageDb/HorecaHit-top.jpg', 
			'size':[utils.image.fit_to_box.init([page_width-4,page_height],os.path.join('/home/raven/git/pages/imageDb/HorecaHit-top.jpg'))[0] + 2,utils.image.fit_to_box.init([page_width,page_height],os.path.join('/home/raven/git/pages/imageDb/HorecaHit-top.jpg'))[1]],
			'x':2,
			'y':page_height - utils.image.fit_to_box.init([page_width,page_height],os.path.join('/home/raven/git/pages/imageDb/HorecaHit-top.jpg'))[1],
			},
		'bottom': 
			{	
			'type' : 'image',
			'file_name': u'/home/raven/git/pages/imageDb/HorecaHit-bottop.jpg', 
			'size':[utils.image.fit_to_box.init([page_width,page_height],os.path.join('/home/raven/git/pages/imageDb/HorecaHit-bottop.jpg'))[0] + 2,utils.image.fit_to_box.init([page_width,page_height],os.path.join('/home/raven/git/pages/imageDb/HorecaHit-bottop.jpg'))[1]], 
			'x':0,
			'y':0,
			},
	}


	dynamic_area = utils.layout.working_area.init(page_size,template)
	template['working area'] = { 
								'type' : 'box',
								'x':dynamic_area[0][0],
								'y':dynamic_area[0][1],
								'size':(dynamic_area[0][2],dynamic_area[0][3])
								}


	if verbose == True:
		for element_name,element_data in template.iteritems():
			#printelement_name
			for property_name,property_value in element_data.iteritems():
				pass
				#print'\t',property_name,property_value
	return(template)