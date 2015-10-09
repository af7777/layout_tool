from reportlab.pdfbase.pdfmetrics import stringWidth

def width(string,font,fsize):
	if string == None:
		string = 'None'
	string_lines_array = []
	for element in string.split('<br/>'):
		string_lines_array.append(stringWidth(element,font,fsize))	
	return(max(string_lines_array))

def height(string,font,fsize,aWidth,leading=1.2):
	lines_count = None
	lines_count = len(simpleSplit(string,font,fsize, aWidth))
	if len(string.split('<br/>')) > lines_count:
		lines_count = len(string.split('<br/>'))
	return (lines_count*fsize+leading)