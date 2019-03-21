#!/usr/bin/python
#-*-encoding:utf-8-*-

__doc__ = """
闭包是一种形式，具体语言支持的形式不一样，但基本含义都一样。
闭包是一个函数体，通常是将这个函数体返回给外部（回调也是外部调用过来），
外部再来调用这个函数体，好处是这个函数体是可以很方便访问函数体外面的一
些变量。拿Python给你解释下：

```python
def closure():
      a = 1
      def func():
            print a
            return a
      return func

b = closure()
b()
```

上面调用closure的时候，返回的是一个函数func，函数可以继续被调用，
然后内部的print语句就被调用了，因为a在closure里面已经定义了，
所以打印的是closure里面的1。那么实际上是完全等价于下面的代码：

```python
class closure(object):
     
    def __init__(self):
        self.a = 1

    def __call__(self):
        print self.a
        return self.a

b = closure()
b()
```
这儿我用了下`__call__`这个python的特殊的方式（表示类的实例可以当成函
数调用）。两种实现，第一种在有些时候会更简单一些。
"""

class array(object) :
    """Simple Array object that support autodiff."""
    def __init__(self, value, name=None):
        self.value = value
        if name:
            self.grad = lambda g : {name : g}

    def __add__(self, other):
        assert isinstance(other, int)
        ret = array(self.value + other)
        ret.grad = lambda g : self.grad(g)
        return ret

    def __mul__(self, other):
        assert isinstance(other, array)
        ret = array(self.value * other.value)
        def grad(g):
            x = self.grad(g * other.value)
            x.update(other.grad(g * self.value))
            return x
        ret.grad = grad
        return ret

def test_grad():
    # some examples
    a = array(1, 'a')
    b = array(2, 'b')
    c = b * a
    d = c + 1
    print d.value
    print d.grad(1)
    # Results
    # 3
    # {'a': 2, 'b': 1}

if __name__ == '__main__':
    test_grad()