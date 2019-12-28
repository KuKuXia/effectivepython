"""
Python中全局解释器锁（GIL）的存在，在任意时刻只允许一个线程在解释器中运行，因此python的多线程不适合处理cpu密集型的任务，想要处理cpu密集型的任务，可以使用多进程模型
使用标准库中multiprocessing.Process，它可以启动进程执行任务操作接口，进程间通信，进程间同步等都与Threading.Thread类似
"""
from multiprocessing import Process
from threading import Thread

import time

x = 1


# 多个子进程之间的内存是独立的
def f(s):
    print(s)
    global x
    x = 5
    print(f'Process output x: {x}')


def f2(q):
    print('F2 Start')
    print("Get the q: ", q.get())
    print('F2 End')


def f3(c):
    print('子进程通过Pipe收到：', c.recv())
    c.send(50)


from decimal import Decimal


def isArmstrong(n):
    a, t = [], n
    while t > 0:
        a.append(t % 10)
        t /= 10
    k = len(a)
    return (sum([Decimal(x) ** k for x in a])) == Decimal(n)


def findArmstrong(a, b):
    print(a, b)
    result = [k for k in range(a, b) if isArmstrong(k)]
    print('%s - %s: %s' % (a, b, result))


def findByThread(*argslist):
    workers = []
    for args in argslist:
        worker = Thread(target=findArmstrong, args=args)
        workers.append(worker)
        worker.start()
    for worker in workers:
        worker.join()


def findByProcess(*argslist):
    workers = []
    for args in argslist:
        worker = Process(target=findArmstrong, args=args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()


if __name__ == '__main__':
    # p = Process(target=f, args=('hello',))
    #
    # p.start()
    # p.join()
    # print(f'Main output x {x}')
    #
    # # 可以用过Queue和Pipe在进程间通信
    #
    # # Queue
    # q = Queue()
    # q.put(1)
    # print(q.get())
    # p2 = Process(target=f2, args=(q,))
    # p2.start()
    # # 延时体现子进程被挂起的
    # time.sleep(2)
    # # 在队列中插入数据，子进程中得到数据，并打印出来
    # q.put(1)
    #
    # # Pipe
    # c1, c2 = Pipe()
    # c1.send('abc')
    # print(c2.recv())
    # c2.send('efg')
    # print(c1.recv())
    #
    # p3 = Process(target=f3, args=(c2,))
    # p3.start()
    #
    # c1.send(55)
    # print("主进程通过Pipe收到：", c1.recv())

    # 多线程 vs 多进程的运行时间
    start = time.time()
    # findByProcess((2000000, 2500000), (2500000, 3000000))
    findByThread((2000000, 2500000), (2500000, 3000000))
    print(time.time() - start)
