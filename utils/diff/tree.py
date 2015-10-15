import os

def project_tree(project_path,name):
	project_path = os.path.join(project_path,name)
	if not os.path.exists(project_path):
		os.makedirs(project_path)
		for d in ['images/source','images/clipped','images/not_clipped','data/adv','data/reg','data/json','images/not_clipped_source']:
			os.makedirs(os.path.join(project_path,d))

if __name__ == "__main__":
	project_tree('/home/raven/gen_projects/','horeca')