#!/usr/bin/python2
# -*- coding: utf-8 -*-

import utils.layout.preflight
import utils.text.preflight
import utils.image.rate
import utils.image.fit_to_box
import flow.text_string
import flow.price_std
from reportlab.lib.units import mm

def init2(template,sync_frames = True):
	if sync_frames == True:
		ref_data = utils.layout.preflight.init(template)
	frame_template = {}
	for obj_name,obj_data in template.iteritems():
		if obj_data['type'] == 'frame':
			x = obj_data['x']
			y = obj_data['y']
			width,height = obj_data['size']

			content = obj_data['frame content']

			text = utils.text.preflight.text(content['text'])
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 9				
			text_width,text_height = flow.text_string.init(text,font,font_size).content_width/mm,flow.text_string.init(text,font,font_size).content_height/mm
			text_x = x +2
			text_y = y +2
			frame_template[str(obj_name) + '_text'] = {	
						'type' : 'text_string',
						'text': text, 
						'x':text_x,
						'y':text_y,
						'font':font,
						'font size':font_size,
						'color':'#000000'
						}
			
			header = utils.text.preflight.header(content['header'])
			font = 'HelveticaNeue_LT_CYR_57_Cond'
			font_size = 12
			header_width,header_height = flow.text_string.init(header,font,font_size).content_width/mm,flow.text_string.init(header,font,font_size).content_height/mm
			header_x = x + 2
			header_y = y + 2 + text_height
			frame_template[str(obj_name) + '_header'] = {	
						'type' : 'text_string',
						'text': header, 
						'x':header_x,
						'y':header_y,
						'font':font,
						'font size':font_size,
						'color':'#000000'
						}

			price = content['price']
			scale = 1
			price_rub = price.split('.')[0]
			try:
				price_kop = price.split('.')[1]
			except IndexError:
				price_kop = '00'
			price_width = flow.price_std.init(price_rub,price_kop,scale = scale).content_width/mm
			price_height = flow.price_std.init(price_rub,price_kop,scale = scale).content_height/mm
			frame_template[str(obj_name) + '_price'] = {
														'type':'price',
														'value':str(price_rub) + '.' + str(price_kop),
														'x':x + width - price_width-2,
														'y':y +2,
														'scale':scale,
														}


			image_path = content['image']['image path']
			print image_path
			image_rate_x,image_rate_y = utils.image.rate.init(image_path)		
			if width > height:
				print 'horizontal frame'
				if image_rate_x == 1:
					cx = 0.5
					cy = 0.45

					image_box_width = width*0.9
					
					if sync_frames == True:
						if len(ref_data[y]['image horiz']['image rate']) > 1:
							print 'multiple horizontal'
							image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
							image_box_y = y + ref_data[y]['image horiz']['max text height'] + 2
							#image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
						#one horizontal image in line
						else:
							image_box_height = (height - text_height - header_height - 2)*cy*2
							image_box_y = y + text_height + header_height + 2

					image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5
					image_y = image_box_y + image_box_height*cy - image_height/2
			

				elif image_rate_y == 1:
					print 'ok'
					cx = 0.5
					cy = 0.4
					
					if sync_frames == True:
						#more than one horizontal image in line
						if len(ref_data[y]['image vert']['image rate']) > 1:
							print 'multiple horizontal'
							image_box_height = (height - ref_data[y]['image vert']['max text height'])*0.9 - 2
							try:
								image_box_y = y + ref_data[y]['image horiz']['max text height']
								image_box_width = width*0.6
							except:
								image_box_y = y + text_height + header_height + 2
								image_box_width = width*0.6
							#image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
						#one horizontal image in line
						else:
							print 'single'
							image_box_height = (height - text_height - header_height)*0.9 - 2
							image_box_y = y + text_height + header_height + 2
							image_box_width = width*0.6

					image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5
					image_y = image_box_y + 2
		
			if width < height:
				print 'vertical frame'
				if image_rate_x == 1:
					cx = 0.5
					cy = 0.4

					image_box_width = width*0.95
					
					if sync_frames == True:
						#more than one horizontal image in line
						if len(ref_data[y]['image horiz']['image rate']) > 1:
							print 'multiple horizontal'
							image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
							image_box_y = y + ref_data[y]['image horiz']['max text height'] + 2
							#image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
						#one horizontal image in line
						else:
							print 'single'
							image_box_height = height - text_height - header_height
							image_box_y = y + text_height + header_height + 2

					image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5
					image_y = image_box_y + image_box_height/2 - image_height/2
			

				elif image_rate_y == 1:
					print 'ok'
					cx = 0.5
					cy = 0.4
					
					image_box_width = width * 0.8

					if sync_frames == True:
						#more than one horizontal image in line
						if len(ref_data[y]['image vert']['image rate']) > 1:
							try:
								print 'multiple horizontal'
								image_box_height = (height - ref_data[y]['image vert']['max text height'])*0.9 - 2
								image_box_y = y + ref_data[y]['image horiz']['max text height'] + 2
								#image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
							except:
								image_box_height = (height - text_height - header_height)*0.9 - 2
								image_box_y = y + text_height + header_height + 2								
						#one horizontal image in line
						else:
							print 'single'
							image_box_height = (height - text_height - header_height)*0.9 - 2
							image_box_y = y + text_height + header_height + 2

					image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5
					image_y = image_box_y + 2

			if int(content['mgb art']) in [192750,330433,530652,530653,296683,299384,143277,184155,256670,488128,138207]:
				image_box_width = width *0.9
				image_box_height = width
				image_box_y = y + text_height + header_height + 2

				image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
				image_x = x + width*cx - image_width/2 + 1.5
				image_y = image_box_y +1
										
			#if int(content['mgb art']) in []:
			#	image_box_width = width *0.9
			#	image_box_height = height - text_height - header_height - 2
			#	image_box_y = y + text_height + header_height + 2

			#	image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
			#	image_x = x + width*cx - image_width/2 + 1.5
			#	image_y = image_box_y
			
			try:
				frame_template[str(obj_name) + '_image'] = {	
							'type' : 'image',
							'file_name': image_path, 
							'size':[image_width,image_height],
							'x':image_x,
							'y':image_y,
							}
			except:
				pass

			if 'HORECA SELECT' in header:
				logo_box_width,logo_box_height = [20,20]
				logo_path = '/home/raven/git/pages/imageDb/horeca/HORECA_SELECT.png'  
				logo_width,logo_height = utils.image.fit_to_box.init([logo_box_width,logo_box_height],logo_path)
				logo_x = x + width - 2 - logo_width + 1
				logo_y = y + 2 + price_height
				frame_template[str(obj_name) + '_horeca_logo1'] = {	
					'type' : 'logo',
					'file_name': logo_path, 
					'size':[logo_width,logo_height],
					'x':logo_x,
					'y':logo_y,
					}

			if int(content['mgb art']) in [281977,295820,322816,322824,269072,192750,330433,530652,530653,296683,299384,530354,286322,488128,330433,138207,530653,296683,284591]:
				logo_box_width,logo_box_height = [15,15]
				logo_path = '/home/raven/git/pages/imageDb/horeca/ZAMOROZCA.png'  
				logo_width,logo_height = utils.image.fit_to_box.init([logo_box_width,logo_box_height],logo_path)
				logo_x = x + width - 2 - logo_width + 1
				logo_y = y + height - 2 - logo_height
				frame_template[str(obj_name) + '_horeca_logo2'] = {	
					'type' : 'logo',
					'file_name': logo_path, 
					'size':[logo_width,logo_height],
					'x':logo_x,
					'y':logo_y,
					}
			if int(content['mgb art']) in [274443]:
				logo_box_width,logo_box_height = [5,5]
				logo_path = '/home/raven/gen_projects/horeca_23/box_20.jpg'  
				logo_width,logo_height = utils.image.fit_to_box.init([logo_box_width,logo_box_height],logo_path)
				logo_x = x + width - logo_width - 4
				logo_y = y + price_height - 2
				frame_template[str(obj_name) + '_box20'] = {	
					'type' : 'logo',
					'file_name': logo_path, 
					'size':[logo_width,logo_height],
					'x':logo_x,
					'y':logo_y,
					}
			if int(content['mgb art']) in [28115]:
				logo_box_width,logo_box_height = [5,5]
				logo_path = '/home/raven/gen_projects/horeca_23/box_4.jpg'  
				logo_width,logo_height = utils.image.fit_to_box.init([logo_box_width,logo_box_height],logo_path)
				logo_x = x + width - logo_width - 4
				logo_y = y + price_height - 2
				frame_template[str(obj_name) + '_box4'] = {	
					'type' : 'logo',
					'file_name': logo_path, 
					'size':[logo_width,logo_height],
					'x':logo_x,
					'y':logo_y,
					}
			if int(content['mgb art']) in [251689]:
				logo_box_width,logo_box_height = [5,5]
				logo_path = '/home/raven/gen_projects/horeca_23/box_12.jpg'  
				logo_width,logo_height = utils.image.fit_to_box.init([logo_box_width,logo_box_height],logo_path)
				logo_x = x + width - logo_width - 4
				logo_y = y + price_height - 2
				frame_template[str(obj_name) + '_box12'] = {	
					'type' : 'logo',
					'file_name': logo_path, 
					'size':[logo_width,logo_height],
					'x':logo_x,
					'y':logo_y,
					}

			if int(content['mgb art']) in [427356,131053]:
				logo_box_width,logo_box_height = [5,5]
				text = 'от '
				font = 'Helvetica Neue LT W1G 55 Roman'
				font_size = 15				
				text_width,text_height = flow.text_string.init(text,font,font_size).content_width/mm,flow.text_string.init(text,font,font_size).content_height/mm
				text_x = x + width - 2 - price_width - text_width
				text_y = obj_data['y'] + 0.35
				frame_template[str(obj_name) + 'vol'] = {	
							'type' : 'text_string',
							'text': text, 
							'x':text_x,
							'y':text_y,
							'font':font,
							'font size':font_size,
							'color':'#204A87'
							}


	for name,data in frame_template.iteritems():
		template[name] = data
	return(template)

def init(template,frame)