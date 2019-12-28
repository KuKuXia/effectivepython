"""
定义装饰器函数，用它来生成一个在原函数基础上添加了新功能的函数，替代原函数
"""
import logging
from functools import WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES, wraps
from inspect import signature
from random import randint

import time


def fibonacci(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]


# 使用函数装饰器实现在原函数基础上添加新功能
# 如何为被装饰的函数保存元数据
# 使用标准库functools中的装饰器wraps装饰内部包裹函数，可以制定将元素的某些属性，更新到包裹函数上面
def memo(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]

    return wrapper


# 如何定义带参数的装饰器
# 提取函数签名，使用inspect.signature
# 带参数的装饰器，也就是根据参数定制化一个装饰器，可以看成生产装饰器的工厂

def typeassert(*ty_args, **ty_kwargs):
    def decorator(func):
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        def wrapper(*args, **kwargs):
            for name, obj in sig.bind(*args, **kwargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError(f'{name} must be {btypes[name]}')
            return func(*args, **kwargs)

        return wrapper

    return decorator


@typeassert(int, str, list)
def type_assert(a, b, c):
    print(a, b, c)


# 如何实现属性可修改的函数装饰器
def warn(timeout):
    def decorator(func):
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout:
                msg = f'{func.__name__}: {used} > {timeout}.'
                logging.warning(msg)
            return res

        def set_timeout(k):
            nonlocal timeout
            timeout = k

        wrapper.setTimeout = set_timeout
        return wrapper

    return decorator


@warn(1.5)
def time_test():
    print('In test')
    while randint(0, 1):
        time.sleep(0.5)


# 使用语法糖
@memo
def fibonacci_normal(n):
    if n <= 1:
        return 1
    return fibonacci_normal(n - 1) + fibonacci_normal(n - 2)


@memo
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count


@memo
def f(a, b=1, c='a'):
    """
    f function
    """
    return a * b + 2, c


if __name__ == '__main__':
    print(fibonacci(50))

    print(memo(fibonacci_normal)(50))
    print(fibonacci_normal(50))

    print(memo(climb)(50, (1, 2, 3)))
    print(climb(50, (1, 2, 3)))

    print(f.__name__)
    print(f.__doc__)
    print(f.__module__)
    print(f.__defaults__)
    print(WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)

    # 检查函数参数

    type_assert(1, 'abc', [1, 2, 3])
    # type_assert('a', 1, [1, 2, 3])  # 报错
    # type_assert('1', 1, 'A')  # 报错

    # 测试函数运行时间
    for _ in range(10):
        time_test()

    # 重新设置装饰器的timeout变量
    time_test.setTimeout(1)
    for _ in range(10):
        time_test()
