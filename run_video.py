#!/usr/bin/python2
# -*- coding: utf-8 -*-


from fonts import fonts
from data import adv_text
from data import reg_text
from templates import video_blank
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
import flow.rectangle

mult = 10
page_size = [192*mult,128*mult]
pdf_dir = (os.path.join(os.getcwd(),'out/pdf'))

offer_data = reg_text.init('/home/raven/gen_projects/horeca_23/images/done/','/home/raven/gen_projects/horeca_23')

fonts.init()

for page_number,page_offers in offer_data.iteritems():
	for stamp in range(0,30):
		template = video_blank.init(page_size)
		template = grid.generic.init(template,page_offers)
		for obj_name,obj_data in template.iteritems():
			frame_template = {}
			#init stage
			width,height = page_size
			border = 10

			#logo
			image_path = '/home/raven/gen_projects/video/template/you_metro.jpg'
			image_box_width = width/2
			image_box_height = height/2
			image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
			
			if stamp == 0:
				image_width = image_width * 0.9
				image_height = image_height * 0.9
				image_x = width/2 - image_width/2
				image_y = height/2 - image_height/2

			elif stamp >= 1 and stamp < 30:
				period = 29
				image_width = image_width * 0.9
				image_height = image_height * 0.9
				step_x = (width*3/4 - width/2) / 60
				step_y = (height/2 - image_height/2 - border) / 60
				print 'steps',step_x,step_y,width
				image_x = image_x + step_x
				image_y = image_y - step_y

			#else:
			#	image_width = image_width * 0.9
			#	image_height = image_height * 0.9
			#	image_x = width*3/4 - image_width/2
			#	image_y = border
			frame_template[str(obj_name) + '_image'] = {	
						'type' : 'image',
						'file_name': image_path, 
						'size':[image_width,image_height],
						'x':image_x,
						'y':image_y,
						}

			frame_template[str(obj_name) + '_rectangle'] = {	
				'type' : 'rectangle', 
				'size':[100,100],
				'x':300,
				'y':300,
				'color': '#204A87'
				}
		for name,data in frame_template.iteritems():
			template[name] = data
			
		generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(stamp) + '.pdf')
		sourceFile = os.path.join('/home/raven/git/pages/out/pdf2/',str(stamp) + '.pdf')
		dest_file = os.path.join('/home/raven/git/pages/out/img/',str(stamp) + '.jpg')
	
		if obj_data['type'] == 'frame2ajfh':
			x = obj_data['x']
			y = obj_data['y']
			width,height = obj_data['size']
			width = page_size[0]
			
			#image animation
			image_path = obj_data['frame content']['image']['image path']
			image_box_width = width/2
			image_box_height = height * 0.8
			image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
			step = (x + width/4 - image_width/2 + image_width)/30
			if stamp == 0:
				image_x = 0 - image_width
			elif stamp > 1 and stamp <= 30:
				image_x = image_x + step
			elif stamp > 30 and stamp <=100:
			 	image_x = x + width/4 - image_width/2
			else:
				image_x = image_x - step
			image_y = y + height/2 - image_height/2

			frame_template[str(obj_name) + '_image'] = {	
						'type' : 'image',
						'file_name': image_path, 
						'size':[image_width,image_height],
						'x':image_x,
						'y':image_y,
						}
			
			#text animation
			start_stamp = 5
			line_shift = 2

			header = obj_data['frame content']['header']
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 80	
			text = utils.text.preflight.text(obj_data['frame content']['text'])
			header = 'яблочный осветленный'
			header_width,header_height = flow.text_string.init(header,font,font_size).content_width/mm,flow.text_string.init(header,font,font_size).content_height/mm
			
			line1 = '1 шт.'
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 60				
			text_width,text_height = flow.text_string.init(line1,font,font_size).content_width/mm,flow.text_string.init(line1,font,font_size).content_height/mm
			
			area = width - (x + width/4 + image_width/2)
			step = (x + width/4 + image_width/2 + area/2)/30
			if stamp >= start_stamp:
				if stamp == start_stamp:
					line1_text_x = width
				elif stamp <= 30 and stamp > start_stamp:
					line1_text_x = line1_text_x - step

				#elif stamp > 30 + start_stamp and stamp <= 100 + start_stamp :
				#	line1_text_x = x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2

				elif stamp > 100 + start_stamp:
					line1_text_x = line1_text_x + step
				
				line1_text_y = y +35
				frame_template[str(obj_name) + '_text_line1'] = {	
							'type' : 'text_string',
							'text': line1, 
							'x':line1_text_x,
							'y':line1_text_y,
							'font':font,
							'font size':font_size,
							'color':'#204A87'
							}

			line2 = 'арт. 426765'
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 60				
			text_width,text_height = flow.text_string.init(line1,font,font_size).content_width/mm,flow.text_string.init(line1,font,font_size).content_height/mm
			
			#step = (x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2)/30

			if stamp >= start_stamp + 2:
				if stamp == start_stamp + 2:
					line2_text_x = width
				elif stamp <= 30 +2 and stamp > start_stamp + 2:
					line2_text_x = line2_text_x - step
				#elif stamp > 30 + start_stamp +2 and stamp <= 100 + start_stamp +2 :
				#	line2_text_x = x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2

				elif stamp > 100 + 2 + start_stamp:
					line2_text_x = line2_text_x + step
				
				line2_text_y = y +35 + text_height
				frame_template[str(obj_name) + '_text_line2'] = {	
							'type' : 'text_string',
							'text': line2, 
							'x':line2_text_x,
							'y':line2_text_y,
							'font':font,
							'font size':font_size,
							'color':'#204A87'
							}
			line3 = '0.97 л'
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 60				
			text_width,text_height = flow.text_string.init(line1,font,font_size).content_width/mm,flow.text_string.init(line1,font,font_size).content_height/mm
			
			#step = (x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2)/30

			if stamp >= start_stamp + 4:
				if stamp == start_stamp + 4:
					line3_text_x = width
				elif stamp <= 30 +4 and stamp > start_stamp + 4:
					line3_text_x = line3_text_x - step 

				#elif stamp > 30 + start_stamp +4 and stamp <= 100 + start_stamp +4 :
				#	line3_text_x = x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2

				elif stamp > 100 + 4 + start_stamp:
					line3_text_x = line3_text_x + step
				
				line3_text_y = y +35 + text_height*2
				frame_template[str(obj_name) + '_text_line3'] = {	
							'type' : 'text_string',
							'text': line3, 
							'x':line3_text_x,
							'y':line3_text_y,
							'font':font,
							'font size':font_size,
							'color':'#204A87'
							}

			header1 = 'яблочный осветлённый'
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 70				
			#header_width,header_height = flow.text_string.init(header1,font,font_size).content_width/mm,flow.text_string.init(header1,font,font_size).content_height/mm
			
			#step = (x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2)/30

			if stamp >= start_stamp + 6:
				if stamp == start_stamp + 6:
					header1_x = width
				elif stamp <= 30 +6 and stamp > start_stamp + 6:
					header1_x = header1_x - step

				#elif stamp > 30 + start_stamp +6 and stamp <= 100 + start_stamp +6 :
				#	header1_x = x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2

				elif stamp > 100 + 6 + start_stamp:
					header1_x = header1_x + step
				
				header1_y = y +35 + text_height*3
				frame_template[str(obj_name) + '_header_line1'] = {	
							'type' : 'text_string',
							'text': header1, 
							'x':header1_x,
							'y':header1_y,
							'font':font,
							'font size':font_size,
							'color':'#204A87'
							}
			header2 = 'Сок "Я"'
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 70				
			#header_width,header_height = flow.text_string.init(header2,font,font_size).content_width/mm,flow.text_string.init(header2,font,font_size).content_height/mm
			
			#step = (x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2)/30

			if stamp >= start_stamp + 8:
				if stamp == start_stamp + 8:
					header2_x = width
				elif stamp <= 30 +8 and stamp > start_stamp + 8:
					header2_x = header2_x - step 

				#elif stamp > 30 + start_stamp +8 and stamp <= 100 + start_stamp +8 :
					#header2_x = x + width/4 + image_width/2 + (width - width/4 + image_width/2)/2 - header_width/2

				elif stamp > 100 + 8 + start_stamp:
					header2_x = header2_x + step
				
				header2_y = y +35 + text_height*3 + header_height
				frame_template[str(obj_name) + '_header_line2'] = {	
							'type' : 'text_string',
							'text': header2, 
							'x':header2_x,
							'y':header2_y,
							'font':font,
							'font size':font_size,
							'color':'#204A87'
							}


			#command = 'gs -dNOPAUSE -sDEVICE=jpeg -dFirstPage=1 -dLastPage=1 -sOutputFile=' + str(dest_file) +' -dJPEGQ=100 -r500 -q ' + str(sourceFile) +' -c quit'
			#os.popen(command)
#	template = frame.generic_video.init(template)
#	generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(page_number) + '_test_1.pdf')

#command = 'pdfunite $(ls ' + '/home/raven/git/pages/out/pdf2/' + ') out.pdf && gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dTextAlphaBits=2 -dGridFitTT=1 -dColorImageResolution=320 -sOutputFile=out_light.pdf out.pdf'
#os.popen(command)
#mencoder "mf:///home/raven/git/pages/out/img/*.jpg" -mf fps=60:type=jpg -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=7000 -vf scale=1920:1080 -force-avi-aspect 1.777 -o /home/raven/git/pages/out/video/movie.avi
