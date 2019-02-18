#!/usr/bin/env python
# -*- coding: utf-8 -*-

# struct 模块用于解决bytes和其它二进制数据类型的转换

# 把一个32位无符号整数变成字节，也就是4个长度的bytes
###################################################
#  笨办法
###################################################
print('============= 笨办法 =============')
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0x00ff0000) >> 16
b3 = (n & 0x0000ff00) >> 8
b4 = (n & 0x000000ff)
print(bytes([b1, b2, b3, b4]))  # b'\x00\x9c@c'

###################################################
#  struct: pack
###################################################
import struct
# '>' 表示字节顺序是big-endian，也就是网络序，'I'表示4字节无符号整数。
print(struct.pack('>I', 10240099))  # b'\x00\x9c@c'

###################################################
#  struct: unpack
###################################################
# I：4字节无符号整数 H：2字节无符号整数
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))  # (4042322160, 32896)


# 练习: 解析windows的位图文件(.bmp)
# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
import base64
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def get_bmp_info(data):
    r = struct.unpack('<ccIIIIIIHH', data[:30])
    return {
        'type': r[0] + r[1],
        'size': r[2],
        'width': r[6],
        'height': r[7],
        'color': r[9]
    }


# {'type': b'BM', 'size': 616, 'width': 28, 'height': 10, 'color': 16}
print(get_bmp_info(bmp_data))
