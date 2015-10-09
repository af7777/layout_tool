def init(template):
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