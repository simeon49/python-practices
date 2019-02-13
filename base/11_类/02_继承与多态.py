#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Bird(Animal):
    def run(self):
        print('Bird is running...')

dog = Dog()
bird = Bird()
animal = Animal()

dog.run()
bird.run()
animal.run()

print(isinstance(dog, Dog)) # True
print(isinstance(dog, Animal)) # True
