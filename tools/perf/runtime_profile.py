"""
装饰器实现对函数整体运行时间的timecall
以及每步函数调用所消耗的时间profile
profilehooks中timecall用装饰器实现了一个计时功能，并可以设置参数
profilehooks中profile返回的数据格式与cProfile返回的数据格式类似

还可以参考使用的工具
timeit
line_profiler
cProfile
自定义装饰器
使用__enter__,__exit__上下文管理器控制计时功能
"""
import time

from profilehooks import timecall, profile


@profile
def test_profile_case():
    time.sleep(1)
    foo()
    time.sleep(0.1)
    bar()
    time.sleep(2.2)


@timecall
def test_timecall_case():
    time.sleep(1)
    foo()
    time.sleep(0.1)
    bar()
    time.sleep(2.2)


@timecall
def foo():
    time.sleep(2.5)


@timecall
def bar():
    time.sleep(1.5)


if __name__ == '__main__':
    # test_timecall_case()
    test_profile_case()
