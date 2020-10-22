# 2020/10/22
# author:xieyudong
from selenium import webdriver
import time

after_cookie = [
    {'domain': '127.0.0.1', 'httpOnly': False, 'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436', 'path': '/',
     'secure': False, 'value': '1603373811'},
    {'domain': '127.0.0.1',
     'httpOnly': False, 'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
     'path': '/', 'secure': False, 'value': '1603373811'},
    {'domain': '127.0.0.1',  'httpOnly': True, 'name': 'beegosessionID', 'path': '/',
     'secure': False, 'value': 'e71ee0801001fcf53259a99c32ec113f'}]
url = 'http://127.0.0.1:8088/login'
driver = webdriver.Chrome()
driver.get(url)
# uanme = driver.find_element_by_name('username').send_keys('libai')
# upwd = driver.find_element_by_name('password').send_keys('sdfsdfsdf')
# loginBtu = driver.find_element_by_tag_name('button').click()

# 在设置之前删除所有cookie信息
driver.delete_all_cookies()
# 设置cookie
for cookie in after_cookie:
    driver.add_cookie(cookie)
# 添加cookie之后 要主动进行刷新
driver.refresh()
time.sleep(3)
driver.quit()
