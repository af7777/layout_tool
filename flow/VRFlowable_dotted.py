from reportlab.platypus.flowables import HRFlowable, Flowable
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color, CMYKColor, PCMYKColor

class init(Flowable):
	def __init__(self,height,thickness = 1):
		Flowable.__init__(self)
		self.height = height
		self.lineWidth = thickness

	def __repr__(self):
	    return "Line(w=%s)" % self.self.lineWidth

	def draw(self):
	    """
	    draw the line
	    """
	    self.canv.setLineWidth(self.lineWidth)
	    self.canv.setDash(self.lineWidth,2)
	    self.canv.setLineCap(1)
	    self.canv.setStrokeColor(HexColor('#d3d3d3'))
	    self.canv.line(0,0,0, self.height*mm)