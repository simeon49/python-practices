#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，
# 优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自
# 己处理事件。正常情况下，优先考虑SAX，因为DOM实在太占内存。

from urllib import request, parse

###################################################
#  sax
###################################################
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def __init__(self):
        self.index = 0

    def start_element(self, name, attrs):
        print('%s<%s attr: %s>' % ('  '* self.index, name, attrs))
        self.index += 1

    def end_element(self, name):
        self.index -= 1
        print('%s</%s>' % ('  ' * self.index, name))

    def char_data(self, text):
        print('%s%s' % ('  ' * self.index, text))


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
