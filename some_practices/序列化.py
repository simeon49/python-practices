import json

def obj2dict(obj):
    d = {}
    d['__class_name__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d

def dict2obj(d):
    if '__class_name__' in d:
        class_name = d.pop('__class_name__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict([(key, value) for key, value in d.items()])
        instance = class_(**args)
    else:
        instance = d
    return instance


class Student(object):
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def __repr__(self):
        return 'Student [name: {}, age: {}, number: {}]'.format(self.name, self.age, self.number)

std1 = Student('Simeon', 21, 1)
d = obj2dict(std1)
print(d)
std = dict2obj(d)
print(std)
