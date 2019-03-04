#-*- encoding:utf-8 -*-
import sys
import subprocess
from enum import Enum
from datetime import datetime

# line = "diff --git a/samples/OpenCV-android-sdk-3.4.1-mini/include/opencv2/core/cuda/warp.hpp b/samples/OpenCV-android-sdk-3.4.1-mini/include/opencv2/core/cuda/warp.hpp"
line_head_len = len("diff --git")
get_filename = lambda line : line[line_head_len:].strip().split()[0][2:]


def is_release_code(source_path):
	if source_path.startswith("src/") or source_path.startswith("include"):
		return True
	return False


class LineClass(Enum):
    space = 1
    diff = 2
    add = 3
    modify = 4
    deleted = 5


def cls_line(line):
	if line.startswith(" "): # 空白行或者是未改动的代码行
		return LineClass.space
	elif line.startswith("diff --git"):
		return LineClass.diff
	elif line.startswith("new"):
		return LineClass.add
	elif line.startswith("deleted"):
		return LineClass.deleted
	else:
		return LineClass.modify


def code_content_diff(branch1, branch2="origin/master"):
	'''不同分支代码内容的不同比较'''
	rev = subprocess.Popen(
	"git diff {} {}".format(branch1, branch2), shell=True, stdout=subprocess.PIPE)
	lines = rev.stdout.readlines()
	i = 0
	total = len(lines)
	update_files = {}
	while i < total:
		line = lines[i]
		state = cls_line(line)
		if state == LineClass.diff:
			fname = get_filename(line)
			j = i + 1
			state = cls_line(lines[j])
			while j < total-1 and cls_line(lines[j]) != LineClass.diff: j += 1
			i, j = j, i
			if not is_release_code(fname): continue
			# print fname
			j += 1
			while not lines[j].startswith("@@"): j += 1
			idx = lines[j].find("@@", 2)
			(pre, modify) = tuple(map(lambda x: tuple(map(int, x[1:].split(','))), lines[j][2:idx].strip().split()))
			print('\033[1;31m{} {}\033[0m'.format(fname, state.name))
			update_files[fname] = state
			if state == LineClass.add:
				print "add code from {} to {}".format(modify[0], modify[0]+modify[1])
				while j < i:
					print lines[j].rstrip()
					j+=1
			elif state == LineClass.modify:
				while j < i:
					if lines[j].startswith("@@"):
						idx = lines[j].find("@@", 2)
						(pre, modify) = tuple(map(lambda x: tuple(map(int, x[1:].split(','))), lines[j][2:idx].strip().split()))
						print('\033[1;31m{}:[{}:{}] {} to [{}:{}]\033[0m'.format(fname,  pre[0], pre[0]+pre[1], state.name, modify[0], modify[0]+modify[1]))
					print lines[j].rstrip()
					j+=1
			elif state == LineClass.deleted:
				print "source code line {}:{} deleted".format(pre[0], pre[0]+pre[1])

			i += 1
		else:	
			i += 1

	print('\n\n\033[1;31msummery\033[0m')
	for k, v in update_files.iteritems():
		print k, v.name
	return update_files

def code_function_diff(branch1, branch2="origin/master"):
	'''用来获取不同分支之间的comment数据的'''
	print('\033[1;31m {} v.s. {}\033[0m'.format(branch2, branch1))
	rev = subprocess.Popen(
		"git log {}..{}".format(branch1, branch2), shell=True, stdout=subprocess.PIPE)
	lines = rev.stdout.readlines()
	i = 0
	total = len(lines)
	submit_dict = dict()
	date_format="%a %b %d %H:%M:%S %Y"
	while i < total:
		line = lines[i].strip()
		if line:
			if line.startswith("commit"):
				[_, commit_id] = line.split()
				submit_dict[commit_id] = dict()
				j = i + 1
				while j < total and not lines[j].strip().startswith("commit"): j+=1
				while i < j:
					line = lines[i].strip()
					if line:
						if line.startswith("Author"):
							submit_dict[commit_id]["Author"] = line[len("Author: "):].split()[1]
						elif line.startswith("Date"):
							str_date = line[len("Date:   "):-len(" +0800")]
							submit_dict[commit_id]["Date"] = str_date # datetime.strptime(str_date, date_format)
						elif line.startswith("Change-Id"):
							submit_dict[commit_id]["Change-Id"] = line.split()[1]
						else:
							submit_dict[commit_id]["comment"] = line
					i += 1
				if i == j: i -= 1
		i += 1
	return submit_dict


if __name__ == '__main__':
	branch2 = "origin/master"
	if len(sys.argv) > 3:
		os.system(sys.argv[3])
	elif len(sys.argv) > 2:
		branch2 = sys.argv[2] 
	else:
		print "python {} before_branch now_branch".format(sys.argv[0])
		exit()
	
	submit_dit = code_function_diff(sys.argv[1], branch2)
	for k, v in submit_dit.iteritems():
		print "{}*{}\t{}".format(k[:10], v["Date"], v["comment"])
