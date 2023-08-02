"""
日志记录至本地文件
"""
import logging

from logging import handlers

# 配置开启记录的最低日志等级，超过该等级的日志将被提示或记录
# logging.basicConfig(level=logging.DEBUG)

# 日志输出字段格式的配置
# logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     level=logging.DEBUG,
#                     filename='test.log',
#                     filemode='a')

# logging日志分级

# logging.debug('debug级别，一般用来打印一些调试信息，级别最低')
# logging.info('info级别，一般用来打印一些正常的操作信息')
# logging.warning('waring级别，一般用来打印警告信息')
# logging.error('error级别，一般用来打印一些错误信息')
# logging.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')

# 模块化配置logging功能
# Logger 暴露了应用程序代码能直接使用的接口
# Handler 将（记录器产生的）日志记录发送至合适的目的地
# Filter 提供了更好的粒度控制，它可以决定输出哪些日志记录
# Formatter 指明了最终输出中日志记录的内容和格式

logger = logging.getLogger('test')
# 设置logger记录哪些日志
logger.setLevel(logging.DEBUG)

# formatter是给handler设置的
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 如果有多个handler记录日志，可以区分配置记录日志的等级
# file_handler = logging.FileHandler('tool_running.log')
# file_handler.setLevel(level=logging.INFO)
# file_handler.setFormatter(formatter)

# 自动分割日志文件
# 有时候我们需要对日志文件进行分割，以方便我们的管理
# 提供了2种形式
# logging.handlers.RotatingFileHandler -> 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
# logging.handlers.TimedRotatingFileHandler -> 按照时间自动分割日志文件
time_rotating_file_handler = handlers.TimedRotatingFileHandler(
    filename=f'test_tool_running.log', when='D')
time_rotating_file_handler.setLevel(logging.DEBUG)
time_rotating_file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
# 设置handler记录哪些日志
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

# logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.addHandler(time_rotating_file_handler)

logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
logger.info('info级别，一般用来打印一些正常的操作信息')
logger.warning('waring级别，一般用来打印警告信息')
logger.error('error级别，一般用来打印一些错误信息')
logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')
