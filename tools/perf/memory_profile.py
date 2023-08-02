"""
引入memory_profiler
查看程序运行时某函数内部各个对象占用内存的消耗

标准库tracemalloc也可查看执行过程中的内存使用情况
不过最好也设计成装饰器模式，不然会侵入已有业务逻辑代码
"""
import gc
import tracemalloc

from memory_profiler import profile


@profile
def mem_list_case():
    tracemalloc.start()

    lots_of_numbers = list(range(1500))
    # lots_of_numbers = list(range(1500))
    x = ['letters'] * (5 ** 10)
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)
    del x
    del lots_of_numbers
    gc.collect()
    return None


if __name__ == "__main__":
    mem_list_case()
