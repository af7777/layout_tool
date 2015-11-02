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

mult = 2
page_size = [(192/mm)*mult,(128/mm)*mult]
pdf_dir = (os.path.join(os.getcwd(),'out/pdf'))

offer_data = reg_text.init('/home/raven/gen_projects/horeca_23/images/done/','/home/raven/gen_projects/horeca_23')
offer = offer_data[offer_data.keys()[0][0]][0]
#print offer[0]
#print offer[0]['price']
fonts.init()
for stamp in range(0,80):
	frame_template = {}
	for page_number,page_offers in offer_data.iteritems():
		template = video_blank.init(page_size)
		template = grid.generic.init(template,page_offers)
	print 'timestamp:',stamp

	#init stage
	width,height = page_size
	h_border = height * 0.025
	v_border = height * 0.025

	#logo
	logo_path = '/home/raven/gen_projects/video/template/you_metro.jpg'
	logo_box_width = width/2 - h_border
	logo_box_height = height/2 - v_border
	logo_width,logo_height = utils.image.fit_to_box.init([logo_box_width,logo_box_height],logo_path)
	logo_width = logo_width
	logo_height = logo_height
	if stamp == 0:
		logo_x = width/2 - logo_width/2
		logo_y = height/2 - logo_height/2
	
	elif stamp >= 1 and stamp <= 30:
		step_x =  (width - h_border - logo_width - width/2 - logo_width/2) / 30
		step_y = (height/2 - logo_height/2 - v_border) / 30
		logo_x = logo_x - step_x
		logo_y = logo_y - step_y

	elif stamp > 30:
		logo_x = width - h_border - logo_width
		logo_y = v_border

	frame_template['static_logo'] = {	
				'type' : 'logo',
				'file_name': logo_path, 
				'size':[logo_width,logo_height],
				'x':logo_x,
				'y':logo_y,
				}
	#back
	back_image_path = '/home/raven/gen_projects/video/template/back.jpg'
	back_image_v_border = height * 0.02 
	if stamp == 0:
		back_image_box_width = width - h_border*2
		back_image_box_height = height - v_border - back_image_v_border
		back_image_width,back_image_height = back_image_box_width,back_image_box_height				
		back_image_x = width/2 - back_image_box_width/2
		back_image_y = height/2 + logo_height/2 + back_image_v_border
	elif stamp >= 1 and stamp <= 30:
		back_image_x = back_image_x
		back_image_y = back_image_y - step_y
	elif stamp > 30 and stamp <= 45:
		back_image_box_width = width- h_border*2
		back_image_box_height = height - v_border*2 - back_image_v_border - logo_height
		back_image_width,back_image_height = back_image_box_width,back_image_box_height				
		back_image_x = width/2 - back_image_width/2
		back_image_y = v_border + logo_height + back_image_v_border
	elif stamp > 45 and stamp <= 60:
		width_step = (width- h_border*2 - width/2 - h_border - width*0.01) / 14
		back_image_box_width = back_image_box_width - width_step
		back_image_box_height = height - v_border*2 - back_image_v_border - logo_height
		back_image_width = back_image_box_width
		back_image_height = back_image_box_height
		back_image_x = h_border
		back_image_y = v_border + logo_height + back_image_v_border	
	elif stamp > 60 and stamp <=75:
		height_step = (height - v_border*2 - back_image_v_border - logo_height - v_border)/15
		step_y = (v_border + logo_height + back_image_v_border - v_border) / 15
		back_image_box_width = width/2 - h_border - width*0.01
		back_image_box_height = back_image_box_height + step_y
		back_image_width = back_image_box_width
		back_image_height = back_image_box_height
		back_image_y = back_image_y - step_y		
	elif stamp > 75:
		back_image_box_width = width/2 - h_border - width*0.01
		back_image_width = back_image_box_width
		back_image_x = h_border
		back_image_y = v_border			

	frame_template['back_image'] = {	
		'type' : 'cover image',
		'file_name': back_image_path, 
		'size':[back_image_width,back_image_height],
		'x':back_image_x,
		'y':back_image_y,
		}

	#phone and email
	if stamp > 60:
		text = "metro-cc.ru"
		font = 'Helvetica Neue LT W1G 55 Roman'
		font_size = 20				
		text_width,text_height = flow.text_string.init(text,font,font_size).content_width/mm,flow.text_string.init(text,font,font_size).content_height/mm
		text_x = h_border + back_image_box_width/2 - text_width/2
		text_y = v_border
		frame_template['contact_text'] = {	
					'type' : 'text_string',
					'text': text, 
					'x':text_x,
					'y':text_y,
					'font':font,
					'font size':font_size,
					'color':'#FFFFFF'
					}
	#slogan
	if stamp >= 31 and stamp <= 45:
		slogan = "ДЛЯ ТЕХ,<br/>KTO DevOps"
		font = 'Helvetica Neue LT W1G 55 Roman'
		font_size = 25				
		slogan_width,slogan_height = flow.text_string.init(slogan,font,font_size).content_width/mm,flow.text_string.init(slogan,font,font_size).content_height/mm
		slogan_x = back_image_x + back_image_width/2 - slogan_width/2
		slogan_y = back_image_y + back_image_height/2 - slogan_height/2
		if stamp == 31:
			slogan = "Д<br/> "
		if stamp == 32:
			slogan = "ДЛ<br/> "
		if stamp == 33:
			slogan = "ДЛЯ<br/> "
		if stamp == 34:
			slogan = "ДЛЯ ТЕ<br/> "
		if stamp == 35:
			slogan = "ДЛЯ ТЕХ<br/> "
		if stamp == 36:
			slogan = "ДЛЯ ТЕХ,<br/> "
		if stamp == 37:
			slogan = "ДЛЯ ТЕХ,<br/>K"
		if stamp == 38:
			slogan = "ДЛЯ ТЕХ,<br/>KT"
		if stamp == 39:
			slogan = "ДЛЯ ТЕХ,<br/>KTO"
		if stamp == 40:
			slogan = "ДЛЯ ТЕХ,<br/>KTO D"
		if stamp == 41:
			slogan = "ДЛЯ ТЕХ,<br/>KTO De"
		if stamp == 42:
			slogan = "ДЛЯ ТЕХ,<br/>KTO Dev"
		if stamp == 43:
			slogan = "ДЛЯ ТЕХ,<br/>KTO DevO"
		if stamp == 44:
			slogan = "ДЛЯ ТЕХ,<br/>KTO DevOp"
		if stamp == 45:
			slogan = "ДЛЯ ТЕХ,<br/>KTO DevOps"

		frame_template['slogan_slogan'] = {	
					'type' : 'text_string_front',
					'text': slogan, 
					'x':slogan_x,
					'y':slogan_y,
					'font':font,
					'font size':font_size,
					'color':'#FFFFFF'
					}
	if stamp == 45:
		slogan_step_x = (back_image_x + back_image_width/2 - slogan_width/2 - h_border - width*0.05) / 15
		slogan_step_y = (back_image_y + back_image_height/2 - slogan_height/2 - (v_border + back_image_box_width*0.05)) / 15		
					
	if stamp > 45 and stamp <= 60:
		slogan_x = slogan_x - slogan_step_x
		slogan_y = slogan_y - slogan_step_y
		print 'slogan y',slogan_step_y
		frame_template['slogan_slogan'] = {	
					'type' : 'text_string_front',
					'text': slogan, 
					'x':slogan_x,
					'y':slogan_y,
					'font':font,
					'font size':font_size,
					'color':'#FFFFFF'
					}
	if stamp > 60:
		slogan = "ДЛЯ ТЕХ,<br/>KTO DevOps"
		font = 'Helvetica Neue LT W1G 55 Roman'
		font_size = 25				
		slogan_width,slogan_height = flow.text_string.init(slogan,font,font_size).content_width/mm,flow.text_string.init(slogan,font,font_size).content_height/mm
		slogan_x = h_border + back_image_box_width*0.05
		slogan_y = back_image_y + back_image_height - back_image_height*0.1 - slogan_height
		frame_template['slogan_slogan'] = {	
					'type' : 'text_string_front',
					'text': slogan, 
					'x':slogan_x,
					'y':slogan_y,
					'font':font,
					'font size':font_size,
					'color':'#FFFFFF'
					}
	
	#frame content 
	#offer image
	if stamp > 31:
		offer_path = '/home/raven/gen_projects/horeca_23/images/done/528155-1-3.tif'
		offer_box_width = logo_width/2
		offer_box_height = (height - v_border*3 - logo_height)*0.8
		offer_width,offer_height = utils.image.fit_to_box.init([offer_box_width,offer_box_height],offer_path)
		offer_width = offer_width
		offer_height = offer_height
		
		image_x = logo_x + logo_width/4 - offer_width/2
		image_y = logo_y + logo_height + v_border + (height - v_border*3 - logo_height)*0.05

		frame_template['offer_image'] = {	
		'type' : 'image',
		'file_name': offer_path, 
		'size':[offer_width,offer_height],
		'x':image_x,
		'y':image_y,
		}

	offer_text = utils.text.preflight.text(offer['header'])
	font = 'HelveticaNeue_LT_CYR_57_Cond'
	font_size = 15				
	offer_text_width,offer_text_height = flow.text_string.init(offer_text,font,font_size).content_width/mm,flow.text_string.init(offer_text,font,font_size).content_height/mm


	text = utils.text.preflight.text(offer['text'])
	font = 'Helvetica Neue LT W1G 55 Roman'
	font_size = 12				
	text_width,text_height = flow.text_string.init(text,font,font_size).content_width/mm,flow.text_string.init(text,font,font_size).content_height/mm
	allign_x = width - int(max([offer_text_width,text_width])) - h_border - 0.5*mm

	#price
	if stamp > 31:
		price = offer['price']
		scale = 1.25
		price_rub = price.split('.')[0]
		try:
			price_kop = price.split('.')[1]
		except IndexError:
			price_kop = '00'
		price_y = image_y
		price_width = flow.price_std.init(price_rub,price_kop,scale = scale).content_width/mm
		price_height = flow.price_std.init(price_rub,price_kop,scale = scale).content_height/mm
		frame_template['price'] = {
								'type':'price',
								'value':str(price_rub) + '.' + str(price_kop),
								'x':allign_x,
								'y':image_y,
								'scale':scale,
								}
	#offer text
	if stamp > 31:
		text_x = allign_x
		text_y = price_y + price_height
		frame_template['offer_text'] = {	
					'type' : 'text_string',
					'text': text, 
					'x':text_x,
					'y':text_y,
					'font':font,
					'font size':font_size,
					'color':'#000000'
					}

	#offer header
		offer_text_x = allign_x
		offer_text_y = text_y + text_height + 0.25*mm
		frame_template['header_text'] = {	
					'type' : 'text_string',
					'text': offer_text, 
					'x':offer_text_x,
					'y':offer_text_y,
					'font':font,
					'font size':font_size,
					'color':'#000000'
					}


	for name,data in frame_template.iteritems():
		template[name] = data
	
	if len(str(stamp)) < 2 :
		fname = '0' + str(stamp)
	else:
		fname = str(stamp)
	generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(fname) + '.pdf')
	sourceFile = os.path.join('/home/raven/git/pages/out/pdf2/',str(fname) + '.pdf')
	dest_file = os.path.join('/home/raven/git/pages/out/img/',str(fname) + '.jpg')
	command = 'gs -dNOPAUSE -sDEVICE=jpeg -dDEVICEWIDTHPOINTS=192 -dDEVICEHEIGHTPOINTS=128 -dFirstPage=1 -dLastPage=1 -sOutputFile=' + str(dest_file) +' -dJPEGQ=100 -r500 -q ' + str(sourceFile) +' -c quit'
	os.popen(command)

#	template = frame.generic_video.init(template)
#	generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(page_number) + '_test_1.pdf')

#command = 'pdfunite $(ls ' + '/home/raven/git/pages/out/pdf2/' + ') out.pdf && gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dTextAlphaBits=2 -dGridFitTT=1 -dColorImageResolution=320 -sOutputFile=out_light.pdf out.pdf'
#os.popen(command)
#mencoder "mf:///home/raven/git/pages/out/img/*.jpg" -mf fps=60:type=jpg -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=7000 -vf scale=1920:1080 -force-avi-aspect 1.777 -o /home/raven/git/pages/out/video/movie.avi
