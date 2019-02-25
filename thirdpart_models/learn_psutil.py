#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    psutil: process and system utilities
    用于编写日常运维工具, 支持 linux/UNIX/OSX/windows等系统

    pip install psutil

    参考: https://github.com/giampaolo/psutil
        https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000
'''

import psutil

###################################################
# 获取CPU信息
###################################################
print(psutil.cpu_count())   # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心数

print(psutil.cpu_times())   # 统计CPU的用户/系统/空闲时间


###################################################
# 实现 top 命令
###################################################
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))


###################################################
# 获取内存信息
###################################################
print(psutil.virtual_memory())

###################################################
# 获取磁盘信息
###################################################
print(psutil.disk_partitions())  # 磁盘分区信息
print(psutil.disk_usage('/'))  # 磁盘使用情况
print(psutil.disk_io_counters())  # 磁盘IO


###################################################
# 获取网络信息
###################################################
print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())  # 获取网络接口信息
