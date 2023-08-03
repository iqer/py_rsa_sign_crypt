# 引入python封装C++ API的功能
# 使用Python调用C++ 使用KDGP(TCP)及KHTP(HTTP)与金证FS2.0系统进行交互
import ctypes
ll = ctypes.cdll.LoadLibrary
lib = ll("./test.so")
lib.foo2(1, 4)
