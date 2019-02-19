#!/usr/bin/env python
# -*- coding: utf-8 -*-

# urllib 是一个网络url请求库, 包含python2 中的(urllib, urllib2), urllib3 则是增加了连接池等功能, 更为强大

from urllib import request, parse

###################################################
#  GET
###################################################
print('============= GET =============')

with request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('  %s: %s' % (k, v))
    print('Data: ', data.decode('utf-8'))


###################################################
#  添加头部
###################################################
print('============= 添加头部 =============')

req = request.Request('http://www.baidu.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('  %s: %s' % (k, v))
    print('Data: ', data.decode('utf-8'))


###################################################
#  Post
###################################################
print('============= POST =============')
email = input('Email for weibo.cn: ')
passwd = input('Password for weibo.cn: ')
login_data = parse.urlencode({
    'username': email,
    'password': passwd,
    'entry': 'mweibo',
    'client_id': '',
    'savestate': '1',
    'ec': '',
    'pagerefer': 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'
})

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header(
    'Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('  %s: %s' % (k, v))
    print('Data: ', data.decode('utf-8'))


###################################################
#  urllib3: 相比urllib增加如下特性:
    # 线程安全
    # 连接池
    # 客户端SSL/TLS验证
    # 文件分部编码上传
    # 协助处理重复请求和HTTP重定位
    # 支持压缩编码
    # 支持HTTP和SOCKS代理
###################################################
import urllib3
print('============= urllib3 =============')
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.baidu.com')
print(r.status)
print(r.data)
