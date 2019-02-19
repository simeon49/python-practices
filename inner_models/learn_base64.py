#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 用64个字符来表示任意二进制数据的方法 (3个字节变为4个字节)
#  ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']

import base64

###################################################
#  b64encode, b64decode
###################################################
r = base64.b64encode(b'binary\x00string')  # b'YmluYXJ5AHN0cmluZw=='
base64.b64decode(r)  # b'binary\x00string'

###################################################
#  urlsafe_b64encode, urlsafe_b64decode:
#   由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
###################################################
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))          # b'abcd++//'
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # b'abcd--__'

print(base64.urlsafe_b64decode('abcd--__'))                # b'i\xb7\x1d\xfb\xef\xff'
