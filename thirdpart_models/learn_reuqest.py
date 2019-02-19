#!/usr/bin/env python
# -*- coding: utf-8 -*-

# requests 是在urllib3的基础上封装的网络url请求库

# pip install requests

import requests

###################################################
#  get
###################################################
print('============ requests.get ============')
r = requests.get('https://www.douban.com/search',
                 params={'q': 'python', 'cat': '1001'},
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'},
                 cookies={'token': 'bear:123'})
print(r.url)    # 实际请求的url
print(r.encoding)       # 'utf-8' requests 自动检测编码
print(r.status_code)    # 200
print(r.headers)        # 头
# print(r.content)        # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
# print(r.text)         # 如果返回为文本
# print(r.json())       # 如果返回为json
print(r.cookies['bid'])        # cookies


###################################################
#  post: 默认使用application/x-www-form-urlencoded对POST数据编码。
###################################################
print('============ requests.post ============')
r = requests.post('https://accounts.douban.com/login',
                 data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.status_code)


###################################################
#  上传文件
###################################################
# print('============ requests.post file ============')
# upload_files = {'file': open('report.xls', 'rb')} # 必须使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
# r = requests.post(url, files=upload_files)
# print(r.status_code)
