import time

class Timeit(object):
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('invoking Timer')

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self.func(instance, *args, **kwargs)

@Timeit
def func():
    time.sleep(1)
    return"invoking function func"

class A(object):
    @Timeit
    def func(self):
        time.sleep(1)
        return'invoking method func'

if __name__ == '__main__':
    a = A()
    print a.func()
    print func()