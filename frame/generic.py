import utils.layout.preflight
import utils.text.preflight
import utils.image.rate
import utils.image.fit_to_box
import flow.text_string
import flow.price_std
from reportlab.lib.units import mm

def init(template,sync_frames = True):
	if sync_frames == True:
		ref_data = utils.layout.preflight.init(template)
	frame_template = {}
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
			text_x = x +2
			text_y = y +2
			frame_template[str(obj_name) + '_text'] = {	
						'type' : 'text_string',
						'text': text, 
						'x':text_x,
						'y':text_y,
						'font':font,
						'font size':font_size,
						'color':'#000000'
						}
			
			header = utils.text.preflight.header(content['header'])
			font = 'HelveticaNeue_LT_CYR_57_Cond'
			font_size = 12
			header_width,header_height = flow.text_string.init(header,font,font_size).content_width/mm,flow.text_string.init(header,font,font_size).content_height/mm
			header_x = x + 2
			header_y = y + 2 + text_height
			frame_template[str(obj_name) + '_header'] = {	
						'type' : 'text_string',
						'text': header, 
						'x':header_x,
						'y':header_y,
						'font':font,
						'font size':font_size,
						'color':'#000000'
						}

			price = content['price']
			scale = 1
			price_rub = price.split('.')[0]
			try:
				price_kop = price.split('.')[1]
			except IndexError:
				price_kop = '00'
			price_width = flow.price_std.init(price_rub,price_kop,scale = scale).content_width/mm
			frame_template[str(obj_name) + '_price'] = {
														'type':'price',
														'value':str(price_rub) + '.' + str(price_kop),
														'x':x + width - price_width-2,
														'y':y +2,
														'scale':scale,
														}


			image_path = content['image']['image path']
			print image_path
			image_rate_x,image_rate_y = utils.image.rate.init(image_path)		
			if width > height:
				print 'horizontal frame'
				if image_rate_x == 1:
					cx = 0.5
					cy = 0.45

					image_box_width = width*0.95
					
					if sync_frames == True:
						if len(ref_data[y]['image horiz']['image rate']) > 1:
							print 'multiple horizontal'
							image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
							image_box_y = y + ref_data[y]['image horiz']['max text height'] + 2
							#image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
						#one horizontal image in line
						else:
							image_box_height = (height - text_height - header_height - 2)*cy*2
							image_box_y = y + text_height + header_height + 2

					image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5
					image_y = image_box_y + image_box_height*cy - image_height/2
			

				elif image_rate_y == 1:
					print 'ok'
					cx = 0.5
					cy = 0.4
					
					if sync_frames == True:
						#more than one horizontal image in line
						if len(ref_data[y]['image vert']['image rate']) > 1:
							print 'multiple horizontal'
							image_box_height = (height - ref_data[y]['image vert']['max text height'])*0.9 - 2
							image_box_y = y + ref_data[y]['image horiz']['max text height']
							#image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
						#one horizontal image in line
						else:
							print 'single'
							image_box_height = (height - text_height - header_height)*0.9 - 2
							image_box_y = y + text_height + header_height + 2

					image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5
					image_y = image_box_y + 2
		
			if width < height:
				print 'vertical frame'
				if image_rate_x == 1:
					cx = 0.5
					cy = 0.4

					image_box_width = width*0.95
					
					if sync_frames == True:
						#more than one horizontal image in line
						if len(ref_data[y]['image horiz']['image rate']) > 1:
							print 'multiple horizontal'
							image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
							image_box_y = y + ref_data[y]['image horiz']['max text height'] + 2
							#image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
						#one horizontal image in line
						else:
							print 'single'
							image_box_height = height - text_height - header_height
							image_box_y = y + text_height + header_height + 2

					image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5
					image_y = image_box_y + image_box_height/2 - image_height/2
			

				elif image_rate_y == 1:
					print 'ok'
					cx = 0.5
					cy = 0.4
					
					if sync_frames == True:
						#more than one horizontal image in line
						if len(ref_data[y]['image vert']['image rate']) > 1:
							print 'multiple horizontal'
							image_box_height = (height - ref_data[y]['image vert']['max text height'])*0.9 - 2
							image_box_y = y + ref_data[y]['image horiz']['max text height'] + 2
							#image_box_height = height - ref_data[y]['image horiz']['max text height'] - 2
						#one horizontal image in line
						else:
							print 'single'
							image_box_height = (height - text_height - header_height)*0.9 - 2
							image_box_y = y + text_height + header_height + 2

					image_width,image_height = utils.image.fit_to_box.init([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5
					image_y = image_box_y + 2

			frame_template[str(obj_name) + '_image'] = {	
					'type' : 'image',
					'file_name': image_path, 
					'size':[image_width,image_height],
					'x':image_x,
					'y':image_y,
					}

	for name,data in frame_template.iteritems():
		template[name] = data
	return(template)