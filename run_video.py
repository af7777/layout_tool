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
page_size = [192*mult/mm/10,128*mult/mm/10]
pdf_dir = (os.path.join(os.getcwd(),'out/pdf'))

offer_data = reg_text.init('/home/raven/gen_projects/horeca_23/images/done/','/home/raven/gen_projects/horeca_23')

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
		step_x =  (width - v_border - logo_width - width/2 - logo_width/2) / 29
		step_y = (height/2 - logo_height/2 - v_border) / 29
		logo_x = logo_x - step_x
		logo_y = logo_y - step_y

	elif stamp > 30:
		logo_x = width - v_border - logo_width
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
		back_image_x = width/2 - back_image_width/2
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
		width_step = (width- h_border*2 - width/2 - h_border - width*0.01) / 15
		back_image_box_width = back_image_box_width - width_step
		back_image_box_height = height - v_border*2 - back_image_v_border - logo_height
		back_image_width = back_image_box_width
		back_image_height = back_image_box_height
		back_image_x = h_border
		back_image_y = v_border + logo_height + back_image_v_border	
	elif stamp > 60:
		back_image_box_width = width/2 - h_border - width*0.01
		back_image_box_height = height - v_border*2 - back_image_v_border - logo_height
		back_image_width = back_image_box_width
		back_image_height = back_image_box_height
		back_image_x = h_border
		back_image_y = v_border + logo_height + back_image_v_border	

		#	back_image_width = back_image_width - width*0.45/30
		#elif stamp >= 45 and stamp < 60:
		#	back_image_y = back_image_y - (height/2 + logo_height/2 + 40 - border)/30
		

	frame_template['back_image'] = {	
		'type' : 'image',
		'file_name': back_image_path, 
		'size':[back_image_width,back_image_height],
		'x':back_image_x,
		'y':back_image_y,
		}


	for name,data in frame_template.iteritems():
		template[name] = data
		
	generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(stamp) + '.pdf')
	sourceFile = os.path.join('/home/raven/git/pages/out/pdf2/',str(stamp) + '.pdf')
	dest_file = os.path.join('/home/raven/git/pages/out/img/',str(stamp) + '.jpg')
	command = 'gs -dNOPAUSE -sDEVICE=jpeg -dDEVICEWIDTHPOINTS=192 -dDEVICEHEIGHTPOINTS=128 -dFirstPage=1 -dLastPage=1 -sOutputFile=' + str(dest_file) +' -dJPEGQ=100 -r500 -q ' + str(sourceFile) +' -c quit'
	os.popen(command)

#	template = frame.generic_video.init(template)
#	generator.page_layout.layout(template,page_size,'/home/raven/git/pages/imageDb/','/home/raven/git/pages/out/pdf2/',str(page_number) + '_test_1.pdf')

#command = 'pdfunite $(ls ' + '/home/raven/git/pages/out/pdf2/' + ') out.pdf && gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dTextAlphaBits=2 -dGridFitTT=1 -dColorImageResolution=320 -sOutputFile=out_light.pdf out.pdf'
#os.popen(command)
#mencoder "mf:///home/raven/git/pages/out/img/*.jpg" -mf fps=60:type=jpg -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=7000 -vf scale=1920:1080 -force-avi-aspect 1.777 -o /home/raven/git/pages/out/video/movie.avi
