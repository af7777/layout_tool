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

import utils.layout.preflight
import utils.text.preflight
import utils.image.rate
import utils.image.fit_to_box
import flow.text_string
import flow.price_std

mult = 3
page_size = [192*mult,128*mult]
pdf_dir = (os.path.join(os.getcwd(),'out/pdf'))

offer_data = reg_text.init('/home/raven/gen_projects/horeca_23/images/done/','/home/raven/gen_projects/horeca_23')

fonts.init()

for page_number,page_offers in offer_data.iteritems():
	print page_offers
	template = horeca.init(page_size)
	template = grid.generic.init(template,page_offers)
	frame_template = {}
	for obj_name,obj_data in template.iteritems():
	
		for stamp in range(0,91): 
			if obj_data['type'] == 'frame':
				x = obj_data['x']
				y = obj_data['y']
				width,height = obj_data['size']
				width = page_size[0]
				print width
				
				image_path = obj_data['frame content']['image']['image path']
				image_box_width = width/2
				image_box_height = height * 0.8
				image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
				if stamp <= 30:
					image_x = 0 + (x + width/4 - image_width/2)/30*stamp
				elif stamp > 30 and stamp <=60:
				 	image_x = x + width/4 - image_width/2
				else:
					image_x = (x + width/4 - image_width/2) - (x + width/4 - image_width/2)/(90 - stamp)
				image_y = y + height/2 - image_height/2
				
				frame_template[str(obj_name) + '_image'] = {	
							'type' : 'image',
							'file_name': image_path, 
							'size':[image_width,image_height],
							'x':image_x,
							'y':image_y,
							}
			for name,data in frame_template.iteritems():
				template[name] = data
				
			generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(stamp) + '.pdf')

#	template = frame.generic_video.init(template)
#	generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(page_number) + '_test_1.pdf')

#command = 'pdfunite $(ls ' + '/home/raven/git/pages/out/pdf2/' + ') out.pdf && gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dTextAlphaBits=2 -dGridFitTT=1 -dColorImageResolution=320 -sOutputFile=out_light.pdf out.pdf'
#os.popen(command)