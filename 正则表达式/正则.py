# 2020/10/20
# author:xieyudong
import re
#1--通配符  .  点 只代表一个元素
strs = 'songqinsi'
#1：需要2个必填参数（正则表达式，处理的字符串） 2：返回类型是一个列表
res1 = re.findall('.',strs)#匹配所有字符
print(res1)#-- ['s', 'o', 'n', 'g', 'q', 'i', 'n']

res2 = re.findall('s.',strs)#匹配字符s后面的第一个字符
print(res2)#--['so', 'si']


# #2 -- *:出现0次或者多次
strs = 'songqinsi'
res3 = re.findall('s*',strs)#匹配字符串中所有的 s 字符,不是 s 字符的 在列表里面展示为空
print(res3)#--['s', '', '', '', '', '', '', 's', '', '']

#3 -- +:出现1次或者多次
res4 = re.findall('s+',strs) # 只匹配字符串中的 s 字符，不是 s 字符的 不匹配,s字符之前必须出现一次
print(res4)# ['s', 's']


#3：.*  和  .+  作用一样  匹配 字符串后面的所有字符
strs = 'songqinsi'
res5 = re.findall('s.*',strs)# 匹配以第一个s开头后面的的所有字符
res6 = re.findall('s.+',strs)
print(res5,res6)#---['songqinsi'] ['songqinsi']


#4  ? 匹配 0个或者1个由前面正则表达式定义的片段，非贪婪方式 和 .+ 或者 .* 一起使用
strs = 'songqinsom'
res7 = re.findall('so(.+?)',strs)#匹配以 so开头，后面的第一个字符
print(res7)#---['n', 'm']

res8 = re.findall('s(.*?)g',strs)#匹配以s开头以g结尾的字符
print(res8)#--- ['on']


# #5 \w 匹配字母数字和下划线
strs = 'songqin123_'
res9 = re.findall('\w',strs)
print(res9)#--['s', 'o', 'n', 'g', 'q', 'i', 'n', '1', '2', '3', '_']
#
# #6 \W 匹配 非 字母数字和下划线
strs = '*&songqin123_'
# res10 = re.findall('\W',strs)
# print(res10)#--- ['*', '&']

res11 = re.findall('\W{2}',strs)#匹配连续2个非字母数字和下划线的字符
print(res11)#--- ['*&']


#7 \d 匹配任意数字，等价于[0-9]

strs = '12345##13566666666#15899999999'
# #获取上面数字的手机号
res12 = re.findall('\d{11}',strs)
res13 = re.findall('\d',strs)
print(res12)#---['13566666666', '15899999999']
print(res13)#---['1', '2', '3', '4', '5', '1', '3', '5', '6', '6', '6', '6', '6', '6', '6', '6', '1', '5', '8', '9', '9', '9', '9', '9', '9', '9', '9']

#8  \D 匹配任意非数字
strs = '12345##13566666666#15899999999'
res14 = re.findall('\D',strs)
print(res14)


# #生成正则表达式对象
strs = '12345##13566666666#15899999999'
reObject = re.compile('\d{11}')#先生成一个正则对象
print(reObject)
print(reObject.findall('135#16988888888###16999999999'))#使用这个正则对象


#  修饰符 re.I --忽略大小写   re.S  -- 使 . 匹配包括换行符在内的所有字符
strs = 'songqinSos\n'
res15 = re.findall('s.',strs,re.I|re.S)
print(res15)#---['so', 'So', 's\n']



