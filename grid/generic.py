import utils.image.rate

def init(template,page_data):
	frame_dict = {}
	working_area_x = template['working area']['x']
	working_area_y = template['working area']['y']
	working_area_width =  template['working area']['size'][0]
	working_area_height =  template['working area']['size'][1]

	if len(page_data) == 1:
		frame_dict['1_frame'] = {
								'x':working_area_x,
								'y':working_area_y,
								'size':[working_area_width,working_area_height],
								'frame content':page_data[0],
								'type':'frame'}

	else:
		image_rates_x = []
		image_rates_y = []
		for frame_data in page_data:
			image_rate = utils.image.rate.init(frame_data['image']['image path'])
			image_rates_x.append(image_rate[0])
			image_rates_y.append(image_rate[1])

		if len(page_data) == 2:
			#both images horizontal
			if image_rates_x.count(1) == len(image_rates_x) or image_rates_x.count(1) != 0:
				for key,data in enumerate(page_data):
					frame_dict[str(key) + '_frame'] = {
										'x':working_area_x,
										'y':working_area_y + working_area_height - working_area_height/2*(key+1),
										'size':[working_area_width,working_area_height/2],
										'frame content':data,
										'type':'frame'
										}
			elif image_rates_x.count(1) == 0:
				for key,data in enumerate(page_data):
					frame_dict[str(key) + '_frame'] = {
										'x':working_area_x+working_area_width/2*key,
										'y':working_area_y,
										'size':[working_area_width/2,working_area_height],
										'frame content':data,
										'type':'frame'
										}

		elif len(page_data) == 3:
			pass

		elif len(page_data) == 4:
			y_key = 0
			line_count = 0
			for key,data in enumerate(page_data):
				frame_dict[str(key) + '_frame'] = {
									'x':working_area_x + working_area_width/2*line_count,
									'y':working_area_y + working_area_height - working_area_height/2*(y_key+1),
									'size':[working_area_width/2,working_area_height/2],
									'frame content':data,
									'type':'frame'
									}
				line_count += 1

				if y_key != 0:
					template[str(key) + '_' + str(y_key) + '_border'] = {
									'x':working_area_x,
									'y':working_area_y + working_area_height - working_area_height/2,
									'width':working_area_width*10,
									'type':'h_dotted_line'
									}
				if line_count == 1:
					template[str(key) + '_' + str(y_key) + '_vborder'] = {
									'x':working_area_x + working_area_width/2*line_count,
									'y':working_area_y,
									'height':working_area_height,
									'type':'v_dotted_line'
									}
				if line_count == 2:
					line_count = 0
					y_key += 1

		elif len(page_data) == 5:
			pass

		elif len(page_data) == 6:
			y_key = 0
			line_count = 0
			for key,data in enumerate(page_data):
				frame_dict[str(key) + '_frame'] = {
									'x':working_area_x + working_area_width/2*line_count,
									'y':working_area_y + working_area_height - working_area_height/3*(y_key+1),
									'size':[working_area_width/2,working_area_height/3],
									'frame content':data,
									'type':'frame'
									}
				line_count += 1

				if y_key != 0:
					template[str(key) + '_' + str(y_key) + '_border'] = {
									'x':working_area_x,
									'y':working_area_y + working_area_height - working_area_height/3*(y_key+1) + working_area_height/3,
									'width':working_area_width*10,
									'type':'h_dotted_line'
									}
				if line_count == 1:
					template[str(key) + '_' + str(y_key) + '_vborder'] = {
									'x':working_area_x + working_area_width/2*line_count,
									'y':working_area_y,
									'height':working_area_height,
									'type':'v_dotted_line'
									}
				if line_count == 2:
					line_count = 0
					y_key += 1
	
		elif len(page_data) == 7:
			pass

		elif len(page_data) == 8:
			pass

		elif len(page_data) == 9:
			y_key = 0
			line_count = 0
			for key,data in enumerate(page_data):
				frame_dict[str(key) + '_frame'] = {
									'x':working_area_x + working_area_width/3*line_count,
									'y':working_area_y + working_area_height - working_area_height/3*(y_key+1),
									'size':[working_area_width/3,working_area_height/3],
									'frame content':data,
									'type':'frame'
									}
				line_count += 1
				if y_key != 0:
					template[str(key) + '_' + str(y_key) + '_border'] = {
									'x':working_area_x,
									'y':working_area_y + working_area_height - working_area_height/3*(y_key+1) + working_area_height/3,
									'width':working_area_width*10,
									'type':'h_dotted_line'
									}
				if line_count == 1 or line_count == 2:
					template[str(key) + '_' + str(y_key) + '_vborder'] = {
									'x':working_area_x + working_area_width/3*line_count,
									'y':working_area_y,
									'height':working_area_height,
									'type':'v_dotted_line'
									}

			
				if line_count == 3:
					line_count = 0
					y_key += 1

	for key,value in frame_dict.iteritems():
		template[key] = value
	return(template)