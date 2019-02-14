#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  ORM: Object Relational Mapping 对象-关系映射
###################################################

from lib.model import Model
from lib.field import IntegerField, StringField

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=123, name='Simeon', email='qixiyi79@gmail.com', password='pwd123')
print(u.id, u.name, u.email, u.password)
u.password = '**********'
u.save()
