#!/usr/bin/python2.7
#!-*-encoding=utf8-*-
import os
import os.path


def print_format(interface_set):
	pass

def get_project_interface(project, func_prefix, is_reverse=False):
	def get_subfiles(srcdir = None):
		filelist= []
		def process_dir(arg, dirname, names):
			for name in names:
				name_path = "{}{}{}".format(dirname, os.sep, name)
				if os.path.islink(name_path):
					os.path.walk(name_path, process_dir, arg)
				elif os.path.isfile(name_path):
					filelist.append(os.path.abspath(name_path))
		if srcdir == None:
			return []
		if isinstance(srcdir, str):
			os.path.walk(srcdir, process_dir, "")
			return filelist
		elif isinstance(srcdir, list):
			for sdir in srcdir:
				os.path.walk(sdir, process_dir, "")
			return filelist

	header_files = filter(lambda x: x.endswith(".h"), get_subfiles("{}/include".format(project)))
	# print header_files
	interface_set = []
	for hfile in header_files:
		with open(hfile) as fd:
			lines = fd.readlines()
			for line in lines:
				line = line.strip()
				if line.startswith("//"): continue
				
				idx = line.find(func_prefix)
				if idx > 0:
					idx_end = line[idx:].find("(")
					if idx_end < 0:
						if line.startswith("#define"):
							interface_set.append(line[idx:].split()[0])
						else:
							interface_set.append(line[idx:])
					else:
						interface_set.append(line[idx: idx + idx_end])
	return sorted(interface_set, reverse=is_reverse)

project_name = "sdk_common"
func_prefix = "cv_common_"

# print get_project_interface(project_name, func_prefix)

sdk_projects = "sdk_common,sdk_face,sdk_segment,sdk_classify,sdk_liveness,sdk_dewatermark,sdk_detect,sdk_hand".split(",")

proj_interface_map = dict()
for proj in sdk_projects:
	print("parsing {} ...".format(proj))
	proj_interface_map[proj] = get_project_interface(proj, func_prefix)

# for k,v in proj_interface_map.items():
# 	print k, v

def howrefactor_project_interface(proj1, branch1, proj2, branch2):
	# TODO:
	# proj1 checkout branch1, proj2 checkout branch2

	proj1_interface = set(get_project_interface(proj1, func_prefix))
	proj2_interface = set(get_project_interface(proj2, func_prefix))
	union_set = proj1_interface | proj2_interface
	intersection = proj1_interface & proj2_interface
	return union_set, intersection
