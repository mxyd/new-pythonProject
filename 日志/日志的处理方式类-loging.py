# 2020/10/19
# author:xieyudong
#日志其实就是一个  .log 文件
import logging
import time
import traceback
# 表示 debug以上的级别都展示，将文件写入到 当前目录的test.log文件下以追加的方式写入
logging.basicConfig(level="DEBUG",filename='./testLog1.log',filemode='a')
logging.debug(time.strftime("%y-%m-%d %H:%M:%S")+'  '+"debug")
logging.info(time.strftime("%y-%m-%d %H:%M:%S")+'  '+"info")
#一般情况下展示后面三个层级，默认级别是warning
logging.warning(time.strftime("%y-%m-%d %H:%M:%S")+'  '+"warning")
logging.error(time.strftime("%y-%m-%d %H:%M%:S")+'  '+"error")
logging.critical(time.strftime("%y-%m-%d %H:%M:%S")+'  '+"critical")
"""
上面这几个的运行结果是：
WARNING:root:warning
ERROR:root:error
CRITICAL:root:critical
"""
