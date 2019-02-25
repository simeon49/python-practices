# -*- coding: utf-8 -*

import time

from orm import Model, AutoIncrementPrimaryField, IntegerField, StringField, FloatField, BooleanField, TextField


class User(Model):
    __table__ = 'user'

    id = AutoIncrementPrimaryField()
    email = StringField(ddl='varchar(50)', unique=True)
    passwd = StringField(ddl='varchar(50)')
    isAdmin = BooleanField()
    name = StringField(ddl='varchar(50)')
    avatar = StringField(ddl='varchar(500)')
    create_time = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blog'

    id = AutoIncrementPrimaryField()
    user_id = IntegerField()
    title = StringField(ddl='varchar(50)', unique=True)
    content = TextField()
    create_time = FloatField(default=time.time)
