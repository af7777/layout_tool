import os

'''mgb art = {'image path':string
			'clipping path':string
			'text':string
			}'''


def init(path):
	pool = {}
	for root,dirs,files in os.walk(path):
		for f in files:
			mgb = f[:f.find('-')]
			pool[mgb] = {'image path' :os.path.join(root,f),
						'clipping path': False,
						'text' = None
						}
	return pool