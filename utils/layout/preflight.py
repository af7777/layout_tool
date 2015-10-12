import utils.text.preflight
import utils.image.rate
import flow.text_string

from reportlab.lib.units import mm

def init(template):
	ref_data_line = {}
	ref_data_row = {}

	for obj_name,obj_data in template.iteritems():
		if obj_data['type'] == 'frame':
			x = obj_data['x']
			y = obj_data['y']
			width,height = obj_data['size']
			content = obj_data['frame content']

			text = utils.text.preflight.text(content['text'])
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 9				
			text_width,text_height = flow.text_string.init(text,font,font_size).content_width/mm,flow.text_string.init(text,font,font_size).content_height/mm

			header = utils.text.preflight.header(content['header'])
			font = 'HelveticaNeue_LT_CYR_57_Cond'
			font_size = 12
			header_width,header_height = flow.text_string.init(header,font,font_size).content_width/mm,flow.text_string.init(header,font,font_size).content_height/mm
			header_x = x + 2
			header_y = y + 2 + text_height

			image_path = content['image']['image path']
			image_rate_x,image_rate_y = utils.image.rate.init(image_path)

			
			if y not in ref_data_line:
				ref_data_line[y] = {'image horiz':{
									'max text height':None,
									'image rate':[]},
									'image vert':{
									'max text height':None,
									'image rate':[]}
									}



			if image_rate_x == 1:			
				if y + 2 + text_height + header_height > ref_data_line[y]['image horiz']['max text height']:
					ref_data_line[y]['image horiz']['max text height'] = 2 + text_height + header_height
				array = ref_data_line[y]['image horiz']['image rate']
				array.append(image_rate_y)
				ref_data_line[y]['image horiz']['image rate'] = array
			
			elif image_rate_y == 1:
				if y + 2 + text_height + header_height > ref_data_line[y]['image vert']['max text height']:
					ref_data_line[y]['image vert']['max text height'] = 2 + text_height + header_height
				array = ref_data_line[y]['image vert']['image rate']
				array.append(image_rate_x)
				ref_data_line[y]['image vert']['image rate'] = array

	print ref_data_line
	return(ref_data_line)