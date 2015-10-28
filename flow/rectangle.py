#!/usr/bin/python2
# -*- coding: utf-8 -*-

from reportlab.platypus.flowables import HRFlowable, Flowable
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color, CMYKColor, PCMYKColor

import utils.text.size

class init(Flowable):	
	def __init__(self,width,height,color):
		Flowable.__init__(self)
		self.width = width*mm
		self.height = height*mm
		self.color = HexColor(color)
		
	def draw(self):
		self.canv.setFillColor(self.color)
		self.canv.setStrokeColor(self.color)		
		self.canv.rect(0,0,10,10,fill=True, stroke=False)
