def init(page_size,template,verbose = False):
	page_width,page_height = [210,297]
	page_coordinates = range(0,page_height)
	for element_name,element_data in template.iteritems():
		element_y0,element_y1 = element_data['y'],element_data['y'] + element_data['size'][1]
		for coordinate in range(int(element_y0),int(element_y1)):
			if coordinate in range(0,page_height):
				page_coordinates.remove(coordinate)
	working_area = [[0,page_coordinates[1],page_width,page_coordinates[-1] - page_coordinates[1]]]
	if verbose == True:
		print 'working area (x0,y0,width,height):',working_area
	return(working_area)