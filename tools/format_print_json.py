#!/usr/bin/env python
#-*-coding=utf-8-*-
import json

jsondict = {"code":0,"data":{"items":[{"id":5053685,"column_id":72,"monographic_id":1234,"related_company_id":0,"related_company_type":"domestic","related_company_name":"","total_words":947,"close_comment":0,"title":"美国大选首场辩论谁赢了？别猜了，答案是社交媒体","catch_title":"美国大选首场辩论赛谁赢了？","summary":"这将是有史以来观看人数最多的美国大选辩论。","cover":"https://pic.36krcnd.com/avatar/201609/27043907/8jtgl8sgn9dnnjum.jpg!feature","related_post_ids":"[\"5050634\",\"5053510\",\"5053578\",\"5053170\",\"5052469\",\"5052817\"]","extraction_tags":"[[\"新闻\",1],[\"信息安全\",2]]","user_id":390347,"published_at":"2016-09-27 12:40:57","created_at":"2016-09-27 12:22:41","updated_at":"2016-09-27 12:54:31","title_mobile":"美国大选首场辩论谁赢了？别猜了，答案是社交媒体","cover_mobile":"https://pic.36krcnd.com/avatar/201609/27043907/8jtgl8sgn9dnnjum.jpg!feature","column":{"id":72,"name":"其他","bg_color":"#000000"},"user":{"id":390347,"name":"杨志芳","avatar_url":"https://krplus-pic.b0.upaiyun.com/4ba5e826e0efa28e31cbd9c0445a0843!480","introduction":"Focus on overseas market."}}],"first":1,"before":1,"current":1,"last":49501,"next":2,"total_pages":49501,"total_items":49501,"limit":1}}
jsonstr = json.dumps(jsondict)

jsondict2 = json.loads(jsonstr)

def print_json(jsondict, level = 0):
	'''The function used for dict to show like a tree
	'''
	assert isinstance(jsondict, dict)

	for i in jsondict.keys():
		print "+-"*level, i, ":",
		if isinstance(jsondict[i], dict):
			print # print a \n
			print_json(jsondict[i], level + 1)
		elif isinstance(jsondict[i], list):
			if isinstance(jsondict[i][0], dict):
				for j in jsondict[i]:
					print #print \n
					print_json(j, level + 1)
			else:
				print jsondict[i]
		else:
			print jsondict[i]

print_json(jsondict2)
