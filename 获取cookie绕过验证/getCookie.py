# 2020/10/22
# author:xieyudong
from selenium import webdriver
"""
启动数据库  docker start mysql_test
启动服务   cd /Users/waitforyou/Documents/文稿 - Wait的MacBook Pro/项目/opms-for-mac/opms-v1-mac
"""
url = 'http://127.0.0.1:8088/login'
driver = webdriver.Chrome()
driver.get(url)
uanme = driver.find_element_by_name('username').send_keys('libai')
upwd = driver.find_element_by_name('password').send_keys('sdfsdfsdf')
loginBtu = driver.find_element_by_tag_name('button').click()

#登录前的cookie
#driver.get_cookies()  获取所有cookie信息
# cookies = driver.get_cookies()
# print(cookies)
"""
cookies的结果：
[
{'domain': '127.0.0.1', 'httpOnly': False, 'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/', 'secure': False, 'value': '1603372275'}, 
{'domain': '127.0.0.1', 'expiry': 1634908274, 'httpOnly': False, 'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/', 'secure': False, 'value': '1603372275'},
{'domain': '127.0.0.1', 'expiry': 1634908273, 'httpOnly': True, 'name': 'beegosessionID', 'path': '/', 'secure': False, 'value': '294d689b6ac819b3a3925c0de1633279'}
]

"""

#driver.get_cookie()  获取所有cookie里面某一项的信息---取cookies里面的name属性的值


# single_cookie = driver.get_cookie('beegosessionID')#例如  取 cookies 里面  name属性值是 beegosessionID 的cookie信息
#
# print(single_cookie)

"""
cookie的值是：
{'domain': '127.0.0.1', 
'expiry': 1634908273, 
'httpOnly': True, 
'name': 'beegosessionID', 
'path': '/', 
'secure': False, 
'value': '294d689b6ac819b3a3925c0de1633279'}
"""

# 登录后的cookie
after_cookie = driver.get_cookies()
print(after_cookie)
"""
after_cookie:
[{'domain': '127.0.0.1', 'httpOnly': False, 'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/', 'secure': False, 'value': '1603372841'},
 {'domain': '127.0.0.1', 'expiry': 1634908840, 'httpOnly': False, 'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/', 'secure': False, 'value': '1603372841'},
 {'domain': '127.0.0.1', 'expiry': 1634908839, 'httpOnly': True, 'name': 'beegosessionID', 'path': '/', 'secure': False, 'value': 'abe5af2765e9e14a605d087180bc8e15'}
 ]
"""

driver.quit()