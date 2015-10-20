#!/usr/bin/python2
# -*- coding: utf-8 -*-

import re
import data.static

def text(string):
	print string
	array = re.findall(r'''\d{5,}''',string)
	if len(array) > 1:
		string = string.replace(array[-1] + ' ',array[-1] + '<br/>')
	elif len(array) == 1:
		string = string.replace(array[0] + ' ',array[0] + '<br/>')
	string = string.replace(' арт.','<br/>арт.')

	#fixing coutries
	replace_list = data.static.coutries_list
	for element in replace_list:
		string = string.replace(element,'<br/>' + element + '<br/>')

	#fixing mass
	string = string.replace('~','<br/>~')
	#['г','кг','л','мл']:
	#array = re.findall(r'\d+ г',string)
	#if len(array) != 0:
	#	string = string.replace(array[0], '<br/>' + str(array[0])+'<br/>')
	#array = re.findall(r'\d+ кг',string)
	#if len(array) != 0:
	#	string = string.replace(array[0], '<br/>' + str(array[0])+'<br/>')
	#array = re.findall(r'\d+ л',string)
	#if len(array) != 0:
	#	string = string.replace(array[0], '<br/>' + str(array[0])+'<br/>')
	#array = re.findall(r'\d+ мл',string)
	#if len(array) != 0:
	#	string = string.replace(array[0], '<br/>' + str(array[0])+'<br/>')

	string = string.replace('различные артикулы','<br/>различные артикулы<br/>')
	
	
	#fixing brand
	brand_array = re.findall(r'[A-Z]+',string)
	if len(brand_array) > 1:
		string = string.replace(brand_array[0],'<br/>' + str(brand_array[0]))
		string = string.replace(brand_array[-1],str(brand_array[1]) + '<br/>')
	elif len(brand_array) == 1:
		string = string.replace(brand_array[0],'<br/>' + str(brand_array[0]) + '<br/>')

	#fixing spaces going with new line
	string = string.replace('<br/> ','<br/>')
	string = string.replace(' <br/>','<br/>')

	#fixing douple <br/>
	string = string.replace('<br/><br/>','<br/>')

	#fixing first <br/> if needed
	if string[:5] == '<br/>':
		string = string[5:] 

	return string

def header(string):
	#fixing brand name
	string = string.replace('HS','HORECA SELECT')
	string = string.replace('Horeca Select','HORECA SELECT')

	array = re.findall(r'''\b[A-Z][A-Z0-9]+\b|\b[А-Я][А-Я0-9]+\b''',string)
	if len(array) > 1:
		string = string.replace(array[-1],array[-1] + '<br/>')
		string = string.replace(array[0],'<br/>' + array[0])
	elif len(array) == 1:
		string = string.replace(array[0],'<br/>' + array[0] + '<br/>')

	array = re.findall(r'''\b[А-Я]+\b''',string)
	if len(array) > 1:
		string = string.replace(array[-1],array[-1] + '<br/>')
		string = string.replace(array[0],'<br/>' + array[0])
	elif len(array) == 1:
		string = string.replace(array[0],'<br/>' + array[0] + '<br/>')

	print string,string[-5:]
	if string[-5:] == '<br/>':
		string = string[:-5]
	#fixing douple <br/>
	string = string.replace('<br/><br/>','<br/>')
	return(string)

