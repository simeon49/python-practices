#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的
str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。
对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很
大概率“猜对”。
当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。

$ pip install chardet
'''

import chardet

###################################################
# 检测 bytes 编码
###################################################
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
print(chardet.detect(b'Hello, world!'))

# {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
print(chardet.detect('这是中文, this is english'.encode('gbk')))

# {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}
print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))