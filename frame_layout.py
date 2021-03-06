import storage_flows
import utils_image
import utils_text

from reportlab.lib.units import mm

def frame_preflight(template):
	ref_data_y = {}
	ref_data_x = {}
	for obj_name,obj_data in template.iteritems():
		if obj_data['type'] == 'frame':
			x = obj_data['x']
			y = obj_data['y']
			width,height = obj_data['size']
			content = obj_data['frame content']

			print 'source text', content['text']
			text = utils_text.text_preflight(content['text'])
			print 'text for layout', text
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 9				
			text_width,text_height = storage_flows.text_string(text,font,font_size).content_width/mm,storage_flows.text_string(text,font,font_size).content_height/mm

			header = utils_text.header_preflight(content['header'])
			font = 'HelveticaNeue_LT_CYR_57_Cond'
			font_size = 12
			header_width,header_height = storage_flows.text_string(header,font,font_size).content_width/mm,storage_flows.text_string(header,font,font_size).content_height/mm
			header_x = x + 2
			header_y = y + 2 + text_height

			image_path = content['image']
			image_rate_x,image_rate_y = utils_image.rate(image_path)

			#if x not in ref_data_x:
			#	ref_data_x[x] = {
			#	}

			if y not in ref_data_y:
				ref_data_y[y] = {
								'max text height':2 + text_height + header_height,
								'image rate x':[image_rate_x]
				}
			else:
				if y + 2 + text_height + header_height > ref_data_y[y]['max text height']:
					ref_data_y[y]['max text height'] = 2 + text_height + header_height
				array = ref_data_y[y]['image rate x']
				array.append(image_rate_x)
				ref_data_y[y]['image rate x'] = array
	return(ref_data_y)

def generic_frame(template,sync_frames = True):
	if sync_frames == True:
		ref_data = frame_preflight(template)
	frame_template = {}
	print template
	for obj_name,obj_data in template.iteritems():
		if obj_data['type'] == 'frame':
			x = obj_data['x']
			y = obj_data['y']
			width,height = obj_data['size']

			content = obj_data['frame content']

			text = utils_text.text_preflight(content['text'])
			font = 'Helvetica Neue LT W1G 55 Roman'
			font_size = 9				
			text_width,text_height = storage_flows.text_string(text,font,font_size).content_width/mm,storage_flows.text_string(text,font,font_size).content_height/mm
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
			
			header = utils_text.header_preflight(content['header'])
			font = 'HelveticaNeue_LT_CYR_57_Cond'
			font_size = 12
			header_width,header_height = storage_flows.text_string(header,font,font_size).content_width/mm,storage_flows.text_string(header,font,font_size).content_height/mm
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
			price_width = storage_flows.Price_std(price_rub,price_kop,scale = scale).content_width/mm
			frame_template[str(obj_name) + '_price'] = {
														'type':'price',
														'value':str(price_rub) + '.' + str(price_kop),
														'x':x + width - price_width-2,
														'y':y +2,
														'scale':scale,
														}


			image_path = content['image']
			image_rate_x,image_rate_y = utils_image.rate(image_path)			
			if width > height:
				print 'horizontal frame'
				if image_rate_x == 1:
					cx = 0.5
					cy = 0.4

					image_box_width = width*0.9
					
					if sync_frames == True:		
						if ref_data[y]['image rate x'].count(1) == len(ref_data[y]['image rate x']):
							if 1 not in ref_data[y]['image rate x']:
								image_box_height = (height - ref_data[y]['max text height']) * cy - 4
								image_y = y + ref_data[y]['max text height'] + 2
							else:
								image_box_height = height - text_height - header_height -2
								image_y = y + text_height + header_height + 2
						else:
							image_box_height = (height - text_height - header_height) * cy - 2
							image_y = y + text_height + header_height
					else:
						image_box_height = (height - text_height - header_height - 2)* cy - 2 
						image_y = y + text_height + header_height 

					image_width,image_height = utils_image.fit_image([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2

				elif image_rate_y == 1:
					cx = 0.5
					image_box_width = width*0.8
					
					if sync_frames == True:		
						if len(ref_data[y]['image rate x']) > 1:
							if 1 not in ref_data[y]['image rate x']:
								image_box_height = height - ref_data[y]['max text height'] - 4
								image_y = y + ref_data[y]['max text height'] + 2
							else:
								print 'ok'
								image_box_height = height - text_height - header_height
								image_y = y + text_height + header_height - 4
						else:
							image_box_height = height - text_height - header_height
							image_y = y + text_height + header_height
					else:
						image_box_height = height - text_height - header_height - 4
						image_y = y + text_height + header_height 

					image_width,image_height = utils_image.fit_image([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2
		
			elif width < height:
				print 'vertical frame'
				if image_rate_x == 1:
					cx = 0.5
					cy = 0.4

					image_box_width = width*0.95
					
					if sync_frames == True:		
						if ref_data[y]['image rate x'].count(1) > 1:
							#if 1 not in ref_data[y]['image rate x']:
							#	image_box_height = (height - ref_data[y]['max text height']) * cy - 4
							#	image_y = y + ref_data[y]['max text height'] + 2
							#else:
							area_height = height - ref_data[y]['max text height'] - header_height - 2
							area_y = y + ref_data[y]['max text height'] + 6
						else:
							area_height = height - text_height - header_height - 4
							area_y = y + text_height + header_height + 4
						#area_y = y + ref_data[y]['max text height'] + 2
						if cy < 0.5:
							image_box_height = area_height*cy*2
							image_width,image_height = utils_image.fit_image([image_box_width,image_box_height],image_path)
							image_y = area_y + area_height*cy - image_height/2

					else:
						image_box_height = (height - text_height - header_height - 2)* cy - 2 
						image_y = y + text_height + header_height 

					image_width,image_height = utils_image.fit_image([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2 + 1.5

				elif image_rate_y == 1:
					cx = 0.5
					cy = 0.4
					image_box_width = width*0.8
					
					if sync_frames == True:		
						#if len(ref_data[y]['image rate x']) > 1:
						#	if 1 not in ref_data[y]['image rate x']:
						#		image_box_height = height - ref_data[y]['max text height'] - 4
						#		image_y = y + ref_data[y]['max text height'] + 2
						#	else:
						area_height = height - text_height - header_height - 2
						area_y = y + text_height + header_height
						if cy < 0.5:
							image_box_height = area_height*0.85
							image_width,image_height = utils_image.fit_image([image_box_width,image_box_height],image_path)
							image_y = area_y + area_height/2 - image_height/2
						#else:
						#	image_box_height = height - text_height - header_height
						#	image_y = y + text_height + header_height
					else:
						image_box_height = height - text_height - header_height - 4
						image_y = y + text_height + header_height 

					image_width,image_height = utils_image.fit_image([image_box_width,image_box_height],image_path)
					image_x = x + width*cx - image_width/2

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