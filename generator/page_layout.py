#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('utf-8')

import flow.text_string
import flow.price_std
import flow.VRFlowable_dotted
import flow.HRFlowable_dotted
import flow.rectangle
import flow.image

from reportlab.lib import colors
from reportlab.lib.colors import HexColor, Color, CMYKColor, PCMYKColor
from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, FrameBreak, PageTemplate, Image, Table, TableStyle, Spacer 

from reportlab.platypus.flowables import HRFlowable, KeepInFrame, Flowable
from reportlab.platypus.doctemplate import LayoutError
from reportlab.pdfbase.pdfmetrics import stringWidth

verbose = True

def layout(data,page_size,imageDb_path,output_dir,file_name):
	def add_image(path,x,y,size):
		#setting image vars
		image_path = path
		x = x
		y = y
		print 'size', size
		size_x = size[0]*mm
		size_y = size[1]*mm

		#setting frame
		image_frame = Frame(x,y,size_x,size_y,id=str(path),bottomPadding=0,topPadding=0,leftPadding=0,rightPadding=0)
		page_frames.append(image_frame)

		#setting object in frame:
		#image = Image(image_path,size_x,size_y,mask='auto')
		image_obj = flow.image.init(image_path,size_x,size_y)
		page_elements.append(image_obj)
		page_elements.append(FrameBreak())

	def add_price(price,x,y,scale = 1):
		price_rub,price_kop = price.split('.')[0],price.split('.')[1]
		price_obj = flow.price_std.init(price_rub,price_kop,scale=scale)
		size_x,size_y = price_obj.content_width,price_obj.content_height
		price_frame = Frame(x*mm,y*mm,size_x,size_y,id=str('price_main'),bottomPadding=0,topPadding=0,leftPadding=0)
		page_frames.append(price_frame)

		page_elements.append(price_obj)
		page_elements.append(FrameBreak())

	def add_text(header,body,x,y,scale = 1):
		text_obj = flow.offer_text(header,body,scale = scale)
		size_x,size_y = text_obj.content_width,text_obj.content_height
		text_frame = Frame(x*mm,y*mm,size_x,size_y,id=str('text_main'),bottomPadding=0,topPadding=0,leftPadding=0)
		page_frames.append(text_frame)

		page_elements.append(text_obj)
		page_elements.append(FrameBreak())

	def add_text_wback(content,x,y,size):
		obj = flow.text_wback(content,x,y,size)
		size_x,size_y = size
		obj_frame = Frame(x*mm,y*mm,size_x,size_y,id=str('obj'),bottomPadding=0,topPadding=0,leftPadding=0)
		page_frames.append(obj_frame)

		page_elements.append(obj)
		page_elements.append(FrameBreak())
	
	def add_h_dotted_line(x,y,width):
		obj = flow.HRFlowable_dotted.init(width)
		obj_frame = Frame(x,y,width,1,id=str('h_dotted_line'),bottomPadding=0,topPadding=0,leftPadding=0)
		page_frames.append(obj_frame)

		page_elements.append(obj)
		page_elements.append(FrameBreak())
	
	def add_v_dotted_line(x,y,lheight):
		obj = flow.VRFlowable_dotted.init(lheight)
		obj_frame = Frame(x,y,0,lheight,id=str('v_dotted_line'),bottomPadding=0,topPadding=0,leftPadding=0)
		page_frames.append(obj_frame)
		
		page_elements.append(obj)
		page_elements.append(FrameBreak())

	def add_text_string(x,y,font,font_size,string,color = '#FFFFFF',border = True):
		obj = flow.text_string.init(string,font,font_size,color,border)
		size_x,size_y = obj.content_width,obj.content_height
		obj_frame = Frame(x*mm,y*mm,size_x,size_y,id=str('text_string'),bottomPadding=0,topPadding=0,leftPadding=0)

		page_frames.append(obj_frame)
		page_elements.append(obj)
		page_elements.append(FrameBreak())

	def add_rectangle(x,y,width,height,color):
		obj = flow.rectangle.init(width,height,color)
		obj_frame = Frame(x,y,width,height,id=str('rectangle'),bottomPadding=0,topPadding=0,leftPadding=0)
		page_frames.append(obj_frame)		
		page_elements.append(obj)
		page_elements.append(FrameBreak())

	#page settings
	page_size_x = page_size[0]*mm
	page_size_y = page_size[1]*mm
	page_left_margin = 0
	page_right_margin = 0

	#page setting containers
	page_frames = []
	page_elements = []

	#layouting
	for name,props in data.iteritems():
		#print props
		if props['type'] == 'image':
			#setting image vars
			image_path = props['file_name']
			image_x = props['x']*mm
			image_y = props['y']*mm
			size_x = props['size'][0]*mm
			size_y = props['size'][1]*mm

			add_image(image_path,image_x,image_y,props['size'])
			#setting frame
			#image_frame = Frame(image_x,image_y,size_x,size_y,id=str(name),bottomPadding=0,topPadding=0,leftPadding=size_x*0.01)
			#page_frames.append(image_frame)

			#setting object in frame:
			#image = Image(image_path,size_x,size_y)
			#page_elements.append(image)
			#page_elements.append(FrameBreak())


		elif props['type'] == 'box' or props['type'] == 'frame':
			x = props['x']*mm
			y = props['y']*mm
			size_x = props['size'][0]*mm
			size_y = props['size'][1]*mm
			box_frame = Frame(x,y,size_x,size_y,id=str(name),bottomPadding=0,topPadding=0,leftPadding=0)
			page_frames.append(box_frame)
			page_elements.append(FrameBreak())
		elif props['type'] == 'h_dotted_line':
			x = props['x']*mm
			y = props['y']*mm
			size_x = props['width']
			size_y = 5*mm
			add_h_dotted_line(x,y,size_x)
		elif props['type'] == 'v_dotted_line':
			x = props['x']*mm
			y = props['y']*mm
			size_y = props['height']
			add_v_dotted_line(x,y,size_y)

	for name,props in data.iteritems():
		if props['type'] == 'rectangle':
			x = props['x']*mm
			y = props['y']*mm
			size_x = props['size'][0]*mm
			size_y = props['size'][1]*mm
			color = props['color']
			add_rectangle(x,y,size_x,size_y,color)	

		if props['type'] == 'price':
			value = props['value']
			x = props['x']
			y = props['y']
			scale = props['scale']
			add_price(value,x,y,scale)
		if props['type'] == 'logo':
			#setting image vars
			image_path = props['file_name']
			image_x = props['x']*mm
			image_y = props['y']*mm
			size_x = int(props['size'][0])*mm
			size_y = int(props['size'][1])*mm

			add_image(image_path,image_x,image_y,props['size'])
			#setting frame
			#image_frame = Frame(image_x,image_y,size_x,size_y,id=str(name),bottomPadding=0,topPadding=0,leftPadding=0)
			#page_frames.append(image_frame)

			#setting object in frame:
			#image = Image(image_path,size_x,size_y)
			#page_elements.append(image)
			#page_elements.append(FrameBreak())

	for name,props in data.iteritems():
		if props['type'] == 'offer text':
			header = props['header']
			body = props['body']
			body = body.replace('Нугар','Нуга')
			x = props['x']
			y = props['y']
			scale = props['scale']
			add_text(header,body,x,y,scale)

		if props['type'] == 'text_string':
			string = props['text']
			#print 'layouting',string
			font = props['font']
			font_size = props['font size']
			x = props['x']
			y = props['y']
			try:
				color = props['color']
				add_text_string(x,y,font,font_size,string,color)
			except:
				add_text_string(x,y,font,font_size,string)

		elif props['type'] == 'text_wback2':
			x = object_data['x']
			y = object_data['y']
			size = object_data['size']
			content = object_data['content']
			add_text_wback(content,x,y,size)

		elif props['type'] == 'frame2':
			for object_data in  props['frame content']:
				if object_data['type'] == 'image':
					x = object_data['x']
					y = object_data['y']
					size = object_data['size']
					path = object_data['file_name']
					add_image(path,x,y,size)
				if object_data['type'] == 'price':
					#print 'price layouting'
					value = object_data['value']
					x = object_data['x']
					y = object_data['y']
					size = object_data['size']
					add_price(value,x,y,scale = 3)
					if verbose == True:
						print 'price:',value,x,y,page_elements
				if object_data['type'] == 'offer text':
					x = object_data['x']
					y = object_data['y']
					size = object_data['size']
					header = object_data['header']
					body = object_data['body']
					add_text(header,body,x,y,size,scale = 1.8)




	# Building page
	current_page = PageTemplate(frames=page_frames)
	doc = BaseDocTemplate(os.path.join(output_dir,str(file_name)),
		pageTemplates=current_page,
		leftMargin=0,
		rightMargin=0,
		topMargin=0,
		bottomMargin=0,
		showBoundary=0,
		cropMarks = False,
		colorSpace='RGB',
		pagesize=(page_size_x,page_size_y))
	doc.addPageTemplates([PageTemplate(id='Test',frames=page_frames)])
	doc.build(page_elements)

