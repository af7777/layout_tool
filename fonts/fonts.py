import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def init():
	pdfmetrics.registerFont(TTFont('Helvetica Neue LT W1G 75 Bold', os.path.join(os.getcwd(),'fonts/storage/Helvetica Neue LT W1G 75 Bold.ttf')))
	pdfmetrics.registerFont(TTFont('Helvetica Neue LT W1G 55 Roman', os.path.join(os.getcwd(),'fonts/storage/Helvetica Neue LT W1G 55 Roman.ttf')))	
	pdfmetrics.registerFont(TTFont('HelveticaNeue_LT_CYR_57_Cond', os.path.join(os.getcwd(),'fonts/storage/HelveticaNeue LT CYR 57 Cond.ttf')))
	pdfmetrics.registerFont(TTFont('HelveticaNeue_LT_CYR_67_MedCn.ttf', os.path.join(os.getcwd(),'fonts/storage/HelveticaNeue LT CYR 67 MedCn.ttf')))
	pdfmetrics.registerFont(TTFont('HelveticaNeue-BoldCr', os.path.join(os.getcwd(),'fonts/storage/HelveticaNeueLTCYR-Bd.ttf')))
	pdfmetrics.registerFont(TTFont('HelveticaNeue-BoldCd', os.path.join(os.getcwd(),'fonts/storage/HelveticaNeueLTPro-BdCn.ttf')))

if __name__ == '__main__':
	init()