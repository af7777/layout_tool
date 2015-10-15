import os
from PIL import Image

def check_path(image_path):
	# gs is needed
	mask_path = os.path.join(os.path.split(image_path)[0],os.path.split(image_path)[1].split('.')[0] + '_mask.png')
	command = 'gm convert ' + str(image_path) + ' -matte -channel matte -clip -negate ' + str(mask_path)
	os.popen(command)
	img = Image.open(mask_path)
	box = img.getbbox()
	os.remove(mask_path)
	if box == (0,0,img.size[0],img.size[1]):
		return False
	else:
		return True

def crop_clip(image_path,cropped_path = None):
	mask_path = os.path.join(os.path.split(image_path)[0],os.path.split(image_path)[1].split('.')[0] + '_mask.png')
	command = 'gm convert ' + str(image_path) + ' -matte -channel matte -clip -negate ' + str(mask_path)
	os.popen(command)
	img = Image.open(mask_path)
	box = img.getbbox()
	img = Image.open(image_path)
	if cropped_path == None:
		img.crop([0+box[0]-1,0+box[1]-1,box[2]+1,box[3]+1]).save(image_path)
	else:
		img.crop([0+box[0]-1,0+box[1]-1,box[2]+1,box[3]+1]).save(cropped_path)
	
	

if __name__ == "__main__":
	print check_path('/home/raven/git/pages/imageDb/clip_test.tif')
	crop_clip('/home/raven/git/pages/imageDb/clip_test.tif','/home/raven/git/pages/imageDb/clip_test_result.tif')