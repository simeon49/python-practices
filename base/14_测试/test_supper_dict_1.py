#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  测试
#     参考: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191629979802b566644aa84656b50cd484ec4a7838000
###################################################
import unittest
from supper_dict import SupperDict


class TestDict(unittest.TestCase):

    def setUp(self):
        print('setup ...')

    def tearDown(self):
        print('tearDown ...')

    def test_init(self):
        d = SupperDict(a=123, b='abc')
        self.assertEqual(d.a, 123)
        self.assertEqual(d.b, 'abc')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = SupperDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = SupperDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = SupperDict()
        with self.assertRaises(KeyError):
            d['not_exist']

    def test_attrerror(self):
        d = SupperDict()
        with self.assertRaises(AttributeError):
            d.not_exist

# 推荐使用命令行运行: python -m unittest mydict_test
if __name__ == '__main__':
    unittest.main()
