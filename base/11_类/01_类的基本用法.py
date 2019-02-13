#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name, score):
        super(Student, self).__init__()
        self.__name = name
        self.__score = score
        Student.count += 1

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 70:
            return 'B'
        else:
            return 'C'

std1 = Student('Tom', 88)
std2 = Student('Jack', 90)

print(Student.count) # 2

print(std1.name, std1.get_grade())  # Tom B
print(std2.name, std2.get_grade())  # Jack A

std1.score = 99
print(std1.score) # 99

try:
    std1.age
except AttributeError as e:
    print('AttributeError:', e)

# 动态添加方法
std1.age = 18
print(std1.age) # 18
