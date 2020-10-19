# 2020/10/19
# author:xieyudong
# try:
#     a = int(input("请输入一个数字："))
#     print(1/a)
# #知道会出现哪些错误，直接不捕获错误，如下所示
# #一个try，后面可以跟多个except，except后面可以跟上 else，和  finally
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as v:
#     print("输入的不是数字",v)
# except:
#     print('未知错误')
# else:
#     print("程序未出现错误")
# finally:
#     print("程序运行结束")

###--------异常处理之使用raise---------####
# try:
#     a = 1
#     b = 2
#     print(a+b)
#     raise ZeroDivisionError  #raise 模拟 异常 ，强制触发后面的except语句
# except:
#      print("输入错误")

###--------assert断言处理异常---------####
#判断12是否是一个int
assert isinstance(12.1,int)