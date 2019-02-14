#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
