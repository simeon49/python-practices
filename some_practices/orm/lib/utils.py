#!/usr/bin/env python
# -*- coding: utf-8 -*-

def camel2underline(camel_format):
    '''
        驼峰格式转下划线格式
    '''
    assert(isinstance(camel_format, str))
    underline_format = ''
    for ch in camel_format:
        underline_format += ch if ch.islower() else '_' + ch.lower()
    return underline_format if not underline_format.startswith('_') else underline_format[1:]

def underline2camel(underline_format):
    '''
        下划线格式转驼峰格式
    '''
    assert(isinstance(underline_format, str))
    camel_format = ''.join(map(lambda s: s.capitalize(), underline_format.split('_')))
    return camel_format

if __name__ == '__main__':
    print(camel2underline('ThisIsAGoodFood'))
    print(underline2camel('_this_is_a_good_food'))
