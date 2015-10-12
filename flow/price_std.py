#!/usr/bin/python2
# -*- coding: utf-8 -*-

from reportlab.platypus.flowables import HRFlowable, Flowable
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import HexColor, Color, CMYKColor, PCMYKColor

import utils.text.size

class init(Flowable):	
	def __init__(self,price_rub,price_kop,items=1,scale=1,x0=0,y0=0):
		Flowable.__init__(self)
		self.scale = scale
		self.price_rub = price_rub
		self.price_kop = price_kop
		self.items = str(items) + '.шт'
		
		self.rub_font = 'HelveticaNeue-BoldCr'
		self.rub_font_size = 28*scale
		self.rub_width = utils.text.size.width(self.price_rub,self.rub_font,self.rub_font_size)

		self.kop_font = 'HelveticaNeue-BoldCr'
		self.kop_font_size = 15*scale
		self.kop_width = utils.text.size.width(self.price_kop,self.kop_font,self.kop_font_size)

		self.splitter_font = 'HelveticaNeue-BoldCr'
		self.splitter_font_size = 28*scale
		self.y_splitter = 4
		
		self.items_font = 'HelveticaNeue_LT_CYR_57_Cond'
		self.items_font_size = 5*scale
		self.items_width = utils.text.size.width(self.items,self.items_font,self.items_font_size)

		self.y_items = 4
		self.x0 = x0
		self.y0 = y0
		self.y0_kop = 10		
		self.stroke_width = 2
		self.scale = scale	

		self.content_width = self.rub_width + max([self.kop_width,self.items_width]) + 5*mm
		self.content_height = self.rub_font_size = 28*scale + 2*mm

		self.body_color = HexColor('#CE1527')
		self.body_color = HexColor('#204A87')
		self.line_color = HexColor('#FFFFFF') 
	def draw(self):

	#price_rub
		y0 = - self.content_height 
		self.canv.setLineWidth(self.stroke_width)
		price_rub_back = self.canv.beginText()
		price_rub_back.setTextOrigin(self.x0,y0)
		price_rub_back.setFont(self.rub_font, self.rub_font_size)
		price_rub_back.setTextRenderMode(2)
		price_rub_back.setFillColor(self.line_color)		
		price_rub_back.setStrokeColor(self.line_color)
		price_rub_back.textLine(self.price_rub)
		self.canv.drawText(price_rub_back)

		self.canv.setLineWidth(0.1)
		price_rub_front = self.canv.beginText()
		price_rub_front.setTextOrigin(self.x0,y0)
		price_rub_front.setFont(self.rub_font, self.rub_font_size)
		price_rub_front.setTextRenderMode(2)
		price_rub_front.setFillColor(self.body_color)		
		price_rub_front.setStrokeColor(self.body_color)
		price_rub_front.textLine(self.price_rub)
		self.canv.drawText(price_rub_front)
		price_rub_width = stringWidth(self.price_rub, self.rub_font, self.rub_font_size) 

	#price_kop
		self.canv.setLineWidth(self.stroke_width)
		price_kop_back = self.canv.beginText()
		price_kop_back.setTextOrigin(price_rub_width,y0+self.y0_kop*self.scale)
		price_kop_back.setFont(self.kop_font, self.kop_font_size)
		price_kop_back.setTextRenderMode(2)
		price_kop_back.setFillColor(self.line_color)		
		price_kop_back.setStrokeColor(self.line_color)
		price_kop_back.textLine(self.price_kop)
		self.canv.drawText(price_kop_back)

		self.canv.setLineWidth(0.1)
		price_kop_front = self.canv.beginText()
		price_kop_front.setTextOrigin(price_rub_width,y0+self.y0_kop*self.scale)
		price_kop_front.setFont(self.kop_font, self.kop_font_size)
		price_kop_front.setTextRenderMode(2)
		price_kop_front.setFillColor(self.body_color)		
		price_kop_front.setStrokeColor(self.body_color)
		price_kop_front.textLine(self.price_kop)
		self.canv.drawText(price_kop_front)

	#splitter
		splitter = ','
		self.canv.setLineWidth(self.stroke_width)
		splitter_back = self.canv.beginText()
		splitter_back.setTextOrigin(price_rub_width,y0+self.y_splitter*self.scale)
		splitter_back.setFont(self.splitter_font, self.splitter_font_size)
		splitter_back.setTextRenderMode(2)
		splitter_back.setFillColor(self.line_color)		
		splitter_back.setStrokeColor(self.line_color)
		splitter_back.textLine(splitter)
		self.canv.drawText(splitter_back)

		self.canv.setLineWidth(0.1)
		splitter_front = self.canv.beginText()
		splitter_front.setTextOrigin(price_rub_width,y0+self.y_splitter*self.scale)
		splitter_front.setFont(self.splitter_font, self.splitter_font_size)
		splitter_front.setTextRenderMode(2)
		splitter_front.setFillColor(self.body_color)		
		splitter_front.setStrokeColor(self.body_color)
		splitter_front.textLine(splitter)
		self.canv.drawText(splitter_front)
		splitter_width = stringWidth(splitter, self.splitter_font, self.splitter_font_size) 
		
	#items
		#self.canv.setLineWidth(self.stroke_width)
		#items_back = self.canv.beginText()
		#items_back.setTextOrigin(price_rub_width+splitter_width,y0+self.y_items*self.scale)
		#items_back.setFont(self.items_font, self.items_font_size)
		#items_back.setTextRenderMode(2)
		#items_back.setFillColor(self.line_color)		
		#items_back.setStrokeColor(self.line_color)
		#splitter_back.textLine(self.items)
		#self.canv.drawText(items_back)

		#self.canv.setLineWidth(0.1)
		#items_front = self.canv.beginText()
		#items_front.setTextOrigin(price_rub_width+splitter_width,y0+self.y_items*self.scale)
		#items_front.setFont(self.items_font, self.items_font_size)
		#items_front.setTextRenderMode(2)
		#items_front.setFillColor(self.body_color)		
		#items_front.setStrokeColor(self.body_color)
		#items_front.textLine(self.items)
		#self.canv.drawText(items_front)
