# 2020/10/21
# author:xieyudong
import requests
import re
import xlwt #给 excel 里面写入内容
import xlrd #读取excel里面的内容
#1-构建请求
#2-解析响应的数据
#3-提取需要的数据
#4-保存数据
web_url = 'https://www.xs4.cc/0_4/'
#获取 web_url 里面的  0_4
url1 = re.findall('https://www.xs4.cc/(.*?)/',web_url)[0]

req = requests.get(web_url)
req.encoding = 'gbk'
#获取书名
bookName = re.findall('<h1>(.*?)</h1>',req.text)[0]
#获取目录信息  catalog：目录的意思
catalog = re.findall('.html">(.*?)</a>',req.text,re.S)
# print(mulu)
#获取所有的目录，因为目录展示最新的九章，所以要从第一章获取的话 ，就要获取目录的下标的，通过下标获取目录信息
# for csub in range(9,len(catalog)):
#     print(catalog[csub])#通过 catalog[csub] 获取所有的目录名称
#获取目录网址信息
catalog_url = re.findall(f'<a href="/{url1}/(.*?).html"',req.text)
# print(catalog_url)
#和目录一样 获取章节的url 从第一张开始
# for curl in range(9,len(catalog_url)):
    # print(catalog_url[curl])
bookDict = {}
for csub in range(9,len(catalog)):
    for curl in range(9, len(catalog_url)):
        bookDict[catalog[csub]] = f'{web_url}{catalog_url[curl]}.html'
# for k,v in bookDict.items():
#     print(k,v)

# 创建excel  给excel 里面写入内容--xlwt
excel = xlwt.Workbook()# 创建一个excel
workSheet = excel.add_sheet("全书网")#创建一个sheet，并给sheet起名为 全书网
workSheet.write(0,0,'目录名')#第一行第一列输入标题 章节
workSheet.write(0,1,'网址')#第一行第一列输入标题 网址
row = 1
for k,v in bookDict.items():
    workSheet.write(row,0,k)#第row 行输入的是 目录
    workSheet.write(row,1,v)#第一列输入的是网址
    row+=1
excel.save(f'./{bookName}.xls')


#读取excel里面的内容--xlrd
#打开excel
data = xlrd.open_workbook(f'./{bookName}.xls')
sheet1 = data.sheets()[0]#返回值是一个列表，读取第一个sheet
for i in range(1,sheet1.nrows):#sheet1.nrows--代表有效行数  从第一行开始到有效行数结束
    #获取单元格内容
    # sheet1.cell_value(行，列) -- 代表 单元格的值(行，列)是坐标  下面表示 读取 第i行第0列 和 第i行第一列
    print(sheet1.cell_value(i,0),sheet1.cell_value(i,1))


