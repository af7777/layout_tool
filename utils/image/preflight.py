#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
from PIL import Image
import shutil

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
	file_name = os.path.split(image_path)[1]
	command = 'gm convert ' + str(image_path) + ' -matte -channel matte -clip -negate ' + str(mask_path)
	os.popen(command)
	img = Image.open(mask_path)
	box = img.getbbox()
	os.remove(mask_path)
	img = Image.open(image_path)
	if cropped_path == None:
		img.crop([0+box[0]-1,0+box[1]-1,box[2]+1,box[3]+1]).save(image_path)
	else:
		img.crop([0+box[0]-1,0+box[1]-1,box[2]+1,box[3]+1]).save(os.path.join(cropped_path,file_name))

def normalize_image(path,dest_path,verbose = False):
	vert = {}
	horiz = {}
	for root,dirs,files in os.walk(path):
		for f in files:
			img = Image.open(os.path.join(root,f))
			image_width,image_height = img.size[0],img.size[1]
			if image_width > image_height:
				horiz[os.path.join(root,f)] = float(image_width)/image_height
			elif image_width < image_height:
				vert[os.path.join(root,f)] = float(image_height)/image_width
	#horizontal reshape
	if len(horiz) > 0:
		min_rate = min(horiz.values())
		print min_rate
		for key,value in horiz.iteritems():
			fname = os.path.split(key)[-1]
			img = Image.open(key)
			image_width,image_height = img.size[0],img.size[1]
			print key,value,image_width,image_height
			print image_height*min_rate,(image_width - image_height*min_rate)/2
			img2 = img.crop((int(0+(image_width - image_height*min_rate)/2), 
							0, 
							int(image_width-(image_width - image_height*min_rate)/2), 
							image_height))
		
			img2.save(os.path.join(dest_path,fname))
	if len(vert) > 0:
		min_rate = float(sum(vert.values())) / len(vert.values()) 
		print min_rate
		for key,value in vert.iteritems():
			fname = os.path.split(key)[-1]
			img = Image.open(key)
			image_width,image_height = img.size[0],img.size[1]
			print key,value,image_width,image_height
			print image_width*min_rate,(image_height - image_width*min_rate)
			img2 = img.crop((0, 
							0, 
							image_width, 
							int(image_height - (image_height - image_width*min_rate))))
		
			print dest_path,file_name
			img2.save(os.path.join(dest_path,fname))

if __name__ == "__main__":
	#for s_root,s_dirs,s_files in os.walk('/home/raven/gen_projects/horeca/images/source/'):
	#	for s_f in s_files:
	#		if check_path(os.path.join(s_root,s_f)) == True:
	#			crop_clip(os.path.join(s_root,s_f),'/home/raven/gen_projects/horeca/images/clipped')
	#		else:
	#			shutil.copy(os.path.join(s_root,s_f),os.path.join('/home/raven/gen_projects/horeca/images/not_clipped_source'))
	normalize_image('/home/raven/gen_projects/horeca_24/imageDB_source/nc/','/home/raven/gen_projects/horeca_24/imageDB_source/ncd/')
	#crop_clip('/home/raven/git/pages/imageDb/clip_test.tif','/home/raven/git/pages/imageDb/clip_test_result.tif')