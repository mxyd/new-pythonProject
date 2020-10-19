# 2020/10/19
# author:xieyudong
import logging
import time
import traceback
logging.basicConfig(filename='./traceback.log',filemode='a',level='DEBUG')
try:
    a = int(input("请输入一个数字："))
    print(1/a)
#知道会出现哪些错误，直接不捕获错误，如下所示
#一个try，后面可以跟多个except，except后面可以跟上 else，和  finally
except ZeroDivisionError as z:
    logging.error(time.strftime("%y-%m-%d %H:%M:%S")+traceback.format_exc())
except ValueError as v:
    logging.error(time.strftime("%y-%m-%d %H:%M:%S") + traceback.format_exc())
except:
    logging.error(time.strftime("%y-%m-%d %H:%M:%S") + traceback.format_exc())
else:
    print("程序未出现错误")
finally:
    print("程序运行结束")

