#!/usr/bin/python2
# -*- coding: utf-8 -*-

from reportlab.platypus.flowables import HRFlowable, Flowable
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color, CMYKColor, PCMYKColor

import utils.text.size

class init(Flowable):
	def __init__(self,path,width,height):
		Flowable.__init__(self)
		self.path = path
		self.width = width
		self.height = height
		self.color = HexColor(color)
		
	def draw(self):		
		self.canv.drawImage(self.path, 0, 0, width=self.width, height=self.height)
