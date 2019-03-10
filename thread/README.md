## 全局锁 与 多线程
全局锁的存在让python的多线程有名无实。解析器每个时候只能让一个线程运行。
但是在某些场景下，如文件读写，响应键盘等阻塞式I/O.
由于受到GIL的保护，所以同一时刻，只有一条线程可以向前执行。

## 协程
协程是一种用户态的轻量级线程，协程的调度完全由用户控制。协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈，直接操作栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。

### Gevent
Gevent是Python中coroutine协程的一种实现，基于Greenlet。其中的monkey库可以直接patch系统的多进程、多线程还有socket的实现，具体的调用方法就是monkey.patch_xxx()，xxx可以是socket，ssl，os，subprocess，thread等。还可以直接调用monkey.patch_all()执行所有的patch。gevent的好处在于可以自动切换协程，一般来说I/O操作比较耗时，那么当一个协程在等待I/O时，它会自动切换到其他协程工作，这样就能够充分利用CPU了。

### 比较常用的函数：

    gevent.spawn(func, args, *kwargs) ：创建greenlet对象
    gevent.joinall(greenlets) ：传入一个greenlet对象列表，开始所有任务并等待完成
    gevent.sleep(seconds) ：挂起secodes秒
    gevent.kill / killall：杀死某个greenlet或一个list的greenlet
    gevent.wait(objects=None, timeout=None, count=None)：进入等待

- http://www.gevent.org/contents.html
- http://sdiehl.github.io/gevent-tutorial/
