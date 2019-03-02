# pyrecipes
工作中，学习中用一些脚本提升开发效率。

## python语法feature demo

1. [pyfeature_defaultval.py](./grammer/pyfeature_defaultval.py)

* 在python中的数据可以分为可变数据类型和不变数据类型。
可变数据类型：像tuple,list,dict之类的变量就是可变数据类型，变量名存储的是一个地址，
该地址指向一个具体的对象，并且不管对变量的值即对象做怎么样的操作，都不会改变变量名存储的地址。
我们把列表作为参数传入一个函数时，在函数内我们对该列表进行了一些改变，由于变量存储的地址没有变
，所以就算我们没有故意通过return语句把该列表传递出来，该列表还是会在函数执行结束后跟着改变的。

* 函数的默认值为可变数据类型的话，会申请一个变量，这个变量地址是固定的，但是值在函数可被改变，
而且还会影响下次调用。

2. [os.path](./grammer/test_os_path.py)

3. 装饰器decorate
* [time wapper](./grammer/timer_wapper.py)
* [decorate](./grammer/decorate.py)

4. [input data](./grammer/input_value.py)

## 常用的python demo

1. [pyflann_ctype](./pyflann_ctype)

对flann库的python封装封装，可以用来学习一下从一个动态库如何封装成为一个python接口。虽然现在有swig等生成工具，但是还是手写的简洁一些，尤其适用于简单的项目。

2. [walk_subfiles.py](./walk_subfiles.py)

进行遍历文件夹下的所有文件的程序

3. [输出json](./tools/format_print_json.py)

格式化输出json
```
{"code":0,"data":{"items":[{"id":5053685,"column_id":72,"monographic_id":1234,"related_company_id":0,"related_company_type":"domestic","related_company_name":"","total_words":947,"close_comment":0,"title":"美国大选首场辩论谁赢了？别猜了，答案是社交媒体","catch_title":"美国大选首场辩论赛谁赢了？","summary":"这将是有史以来观看人数最多的美国大选辩论。","cover":"https://pic.36krcnd.com/avatar/201609/27043907/8jtgl8sgn9dnnjum.jpg!feature","related_post_ids":"[\"5050634\",\"5053510\",\"5053578\",\"5053170\",\"5052469\",\"5052817\"]","extraction_tags":"[[\"新闻\",1],[\"信息安全\",2]]","user_id":390347,"published_at":"2016-09-27 12:40:57","created_at":"2016-09-27 12:22:41","updated_at":"2016-09-27 12:54:31","title_mobile":"美国大选首场辩论谁赢了？别猜了，答案是社交媒体","cover_mobile":"https://pic.36krcnd.com/avatar/201609/27043907/8jtgl8sgn9dnnjum.jpg!feature","column":{"id":72,"name":"其他","bg_color":"#000000"},"user":{"id":390347,"name":"杨志芳","avatar_url":"https://krplus-pic.b0.upaiyun.com/4ba5e826e0efa28e31cbd9c0445a0843!480","introduction":"Focus on overseas market."}}],"first":1,"before":1,"current":1,"last":49501,"next":2,"total_pages":49501,"total_items":49501,"limit":1}}
```


```
code : 0
data :
+- total_items : 49501
+- last : 49501
+- items :
+-+- total_words : 947
+-+- updated_at : 2016-09-27 12:54:31
+-+- published_at : 2016-09-27 12:40:57
+-+- id : 5053685
+-+- extraction_tags : [["新闻",1],["信息安全",2]]
+-+- title_mobile : 美国大选首场辩论谁赢了？别猜了，答案是社交媒体
+-+- user_id : 390347
+-+- title : 美国大选首场辩论谁赢了？别猜了，答案是社交媒体
+-+- column_id : 72
+-+- related_company_type : domestic
+-+- catch_title : 美国大选首场辩论赛谁赢了？
+-+- cover_mobile : https://pic.36krcnd.com/avatar/201609/27043907/8jtgl8sgn9dnnjum.jpg!feature
+-+- close_comment : 0
+-+- related_company_name : 
+-+- monographic_id : 1234
+-+- related_company_id : 0
+-+- user :
+-+-+- introduction : Focus on overseas market.
+-+-+- avatar_url : https://krplus-pic.b0.upaiyun.com/4ba5e826e0efa28e31cbd9c0445a0843!480
+-+-+- id : 390347
+-+-+- name : 杨志芳
+-+- column :
+-+-+- bg_color : #000000
+-+-+- id : 72
+-+-+- name : 其他
+-+- created_at : 2016-09-27 12:22:41
+-+- cover : https://pic.36krcnd.com/avatar/201609/27043907/8jtgl8sgn9dnnjum.jpg!feature
+-+- summary : 这将是有史以来观看人数最多的美国大选辩论。
+-+- related_post_ids : ["5050634","5053510","5053578","5053170","5052469","5052817"]
+- total_pages : 49501
+- next : 2
+- current : 1
+- limit : 1
+- first : 1
+- before : 1
```

## python实现的算法类
1. 信息论
* [pearsonsim](./pearsonsim.py)
* [possion](./possion.py)
* [shanno_entropy](./shanno_entropy)
* [similarity](./similarity.py)

2. [全排列](./perm.py)
全排列的方法很多，其中[Heap's algorithm](https://en.wikipedia.org/wiki/Heap%27s_algorithm)是交换次数最少，最快的全排列算法。

3. [huffman](./huffman.py)