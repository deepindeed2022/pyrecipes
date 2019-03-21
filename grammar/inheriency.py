#!/usr/bin/python
#-*-encoding:utf-8-*-


class Init(object):

    def __init__(self, value):
        self.val = value
        print "Init", self.val


class Mul5(Init):

    def __init__(self, val):
        super(Mul5, self).__init__(val)
        print "Mul5 Before:", self.val
        self.val *= 5
        print "Mul5", self.val


class Add2(Init):

    def __init__(self, val):
        super(Add2, self).__init__(val)
        print "Add2 Before:", self.val
        self.val += 2
        print "Add2", self.val


# 继承多个父类的时候，从后往前初始化父类
class Pro(Mul5, Add2):
    pass


class Incr(Pro):

    def __init__(self, val):
        super(Pro, self).__init__(val)
        self.val += 1
        print "Incr", self.val

"""
             --> Mul5--
            /          \
Incr -> Proc             Init
            \          /
             --> Add2--
"""
p = Incr(5)
print(p.val)

'''output result as following:
init 5
Add2 Before: 5
Add2 7
Mul5 Before: 7
Mul5 35
Incr 36
36
'''

"""
总结： 继承初始化，从底往上； 同一层，先右再左；
"""
