from reportlab.platypus.flowables import HRFlowable, Flowable
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import HexColor, Color, CMYKColor, PCMYKColor

import utils.text.size

class init(Flowable):
	def __init__(self,string,font_name,font_size,color=HexColor('#FFFFFF'),color_space = 'RGB',x0=0,y0=0,border=True):
		Flowable.__init__(self)

		self.stroke_width = 0.1
		self.border = border
		self.border_width = 2
		self.border_color = HexColor('#FFFFFF')
		self.interline = 0.5*mm

		self.text = string
		#print self.text
		self.text_font = font_name
		self.text_font_size = font_size
		self.color = color

		self.content_width = utils.text.size.width(self.text,self.text_font,self.text_font_size)
		self.content_height = len(self.text.split('<br/>'))*self.text_font_size + (len(self.text.split('<br/>')) -1)*self.interline

	def draw(self):
		if self.border == True:
			textobject_static_back = self.canv.beginText()	
			self.canv.setLineWidth(self.border_width)
			textobject_static_back.setTextRenderMode(2)	
			textobject_static_back.setCharSpace(0.2)
			textobject_static_back.setCharSpace(0)
			
			x0 = 0
			y0 = 0 - 10  #hardcoded to adjust content size to real size
			textobject_static_back.setTextOrigin(x0,y0)
			textobject_static_back.setFont(self.text_font,self.text_font_size)
			
			for line in self.text.split('<br/>'):
				self.canv.setLineWidth(self.border_width)
				textobject_static_back.setFillColor(self.border_color)	
				textobject_static_back.setStrokeColor(self.border_color)
				textobject_static_back.setTextOrigin(x0,y0)
				textobject_static_back.textLine(line)
				
				y0 = y0 - self.text_font_size - self.interline
			self.canv.drawText(textobject_static_back)

		textobject_static = self.canv.beginText()	
		self.canv.setLineWidth(self.stroke_width)
		textobject_static.setTextRenderMode(2)	
		textobject_static.setCharSpace(0.2)
		textobject_static.setCharSpace(0)
		
		x0 = 0
		y0 = 0 - 10  #hardcoded to adjust content size to real size
		textobject_static.setTextOrigin(x0,y0)
		textobject_static.setFont(self.text_font,self.text_font_size)
		
		for line in self.text.split('<br/>'):
			self.canv.setLineWidth(self.stroke_width)
			textobject_static.setFillColor(self.color)	
			textobject_static.setStrokeColor(self.color)
			textobject_static.setTextOrigin(x0,y0)
			textobject_static.textLine(line)
			
			y0 = y0 - self.text_font_size - self.interline
		self.canv.drawText(textobject_static)