## 运行环境
python 2.7

cd src
直接在命令行中运行`python main.py`

### 测试用例输入
	Manager.book[site][hash_key]
	> Error:the booking is invalid!
	U001 2016-06-02 22:00~22:00 A
	> Error:the booking is invalid!
	U002 2017-08-01 19:00~22:00 A
	> Success:the booking is accepted!
	U003 2017-08-02 13:00~17:00 B
	> Success:the booking is accepted!
	U004 2017-08-03 15:00~16:00 C
	> Success:the booking is accepted!
	U005 2017-08-05 09:00~11:00 D
	> Success:the booking is accepted!

### 打印汇总结果

收入汇总
---
场地:A
2017-08-01 19:00~22:00 200元
小计:200元

场地:B
2017-08-02 13:00~17:00 200元
小计:200元

场地:C
2017-08-03 15:00~16:00 50元
小计:50元

场地:D
2017-08-05 09:00~11:00 80元
小计:80元

---
总计:530


## 运行单元测试
cd test
`python test_util.py`
`python test_main.py`
