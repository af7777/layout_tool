from PIL import Image

def init(box_size,image_path,verbose = False):
	box_width,box_height = box_size[0],box_size[1]
	
	img = Image.open(image_path)
	image_width,image_height = img.size[0],img.size[1]
		
	if verbose == True:
		print 'Inage path',image_path
		print 'Box size:',box_width,box_height
		print 'Image size:',image_width,image_height

	if box_width != None and box_height != None:
		if image_width > image_height:
			rate = float(image_height) / float(image_width)
			size_x = box_width
			size_y = box_width * rate
			if size_y > box_width:
				size_x = box_height
				size_y = box_height * rate

		elif image_width < image_height:
			rate = float(image_width) / float(image_height)
			size_x = box_height * rate
			size_y = box_height
			if size_y > box_height:
				size_x = box_width * rate
				size_y = box_width
		else:
			size_x = min([box_width,box_height])
			size_y = min([box_width,box_height])

	#check if image actually fits box
	
	if verbose == True:
			print 'Picture in box:',size_x,size_y
	return(size_x,size_y)