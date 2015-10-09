from PIL import Image

def init(image_path):
	img = Image.open(image_path)
	image_width,image_height = img.size[0],img.size[1]
	if image_width > image_height:
		rate = [1,float(image_height) / image_width]
	elif image_width < image_height:
		rate = [float(image_width)/image_height,1]
	else:
		rate = [1,1]
	return(rate)