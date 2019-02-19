#!/usr/bin/env python
# -*- coding: utf-8 -*

# 摘要算法: 又称哈希算法, 散列算法

target_str = '''
Dear son...
孩子…
The day that you see me old and I am already not， have patience and try to understand me …
哪天你看到我日渐老去，身体也渐渐不行，请耐着性子试着了解我……
If I get dirty when eating… if I cannot dress… have patience.
如果我吃的脏兮兮，如果我不会穿衣服……有耐性一点……
Remember the hours I spent teaching it to you.
你记得我曾花多久时间教你这些事吗?
If， when I speak to you，I repeat the same things thousand and one times…
如果，当我一再重复述说
Do not interrupt me… listen to me
同样的事情…不要打断我，听我说….
When you were small， I had to read to you thousand and one times the same story until you get to sleep…
你小时候，我必须一遍又一遍的读着同样的故事，直到你静静睡着……..
When I do not want to have a shower，neither shame me nor scold me…
当我不想洗澡，不要羞辱我也不要责骂我……
Remember when I had to chase you with thousand excuses I invented， in order that you wanted to bath…
你记得小时后我曾编出多少理由，只为了哄你洗澡…..
When you see my ignorance on new technologies… give me the necessary time and not look at me with your mocking smile…
当你看到我对新科技的无知，给我一点时间，不要挂着嘲弄的微笑看着我
I taught you how to do so many things… to eat good， to dress well… to confront life…
我曾教了你多少事情啊….如何好好的吃，好好的穿…如何面对你的生命……
When at some moment I lose the memory or the thread of our conversation…
如果交谈中我忽然失忆不知所云，
let me have the necessary time to remember…
给我一点时间回想…
and if I cannot do it，
如果我还是无能为力，
do not become nervous…　
请不要紧张…..
as the most important thing is not my conversation but surely to be with you and to have you listening to me…
对我而言重要的不是对话，而是能跟你在一起，和你的倾听…..
'''

###################################################
#  md5: 结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
###################################################
import hashlib

# 方法1
md5 = hashlib.md5()
md5.update(target_str.encode('utf-8'))
print(md5.hexdigest())      # f54f7629fdf0b2e296e57bdd4c745cf3

# 方法2: 适用于子串很长
md5_1 = hashlib.md5()
s = target_str
while True:
    md5_1.update(s[:1024].encode('utf-8'))
    if len(s) <= 1024:
        break
    s = s[1024:]
print(md5_1.hexdigest())    # f54f7629fdf0b2e296e57bdd4c745cf3


###################################################
#  sha1: SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示,
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
###################################################
sha1 = hashlib.sha1()
sha1.update(target_str.encode('utf-8'))
print(sha1.hexdigest())     # 71f3691b8ce8d9b6654252e2a01e87ff9998d4fc

sha256 = hashlib.sha256()
sha256.update(target_str.encode('utf-8'))
# fc482a7a6a9e04c86405999f529f2f3bf358ba532384bcb1a224d77b059fc2c1
print(sha256.hexdigest())


###################################################
#  保存用户密码的安全:
###################################################
import random

print('============ 保存用户密码的安全1 ============')

db = {}
calculate_pwd = None

class User(object):

    def __init__(self, name, password):
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.name = name
        self.pwd = self.salt + calculate_pwd(self.salt, password)


def save(user):
    db[user.name] = { 'name': user.name, 'pwd': user.pwd }

def login(username, password):
    user = db[username]
    if not user:
        return False
    salt = user['pwd'][:20]
    return calculate_pwd(salt, password) == user['pwd'][20:]


def method(salt, password):
    md5 = hashlib.md5()
    md5.update((salt + password).encode('utf-8'))
    return md5.hexdigest()


calculate_pwd = method

save(User('Tom', '123456'))
save(User('Jeck', 'pwd_abcd'))
save(User('Bob', 'bob456'))
print(db)

assert login('Tom', '123456')
assert login('Jeck', 'pwd_abcd')
assert not login('Bob', 'bad_password')


###################################################
#  使用hmac 保存用户密码的安全:
###################################################
import hmac

print('============ 使用hmac 保存用户密码的安全: ============')


def method1(salt, password):
    return hmac.new(salt.encode('utf-8'), password.encode('utf-8'), 'sha256').hexdigest()

calculate_pwd = method1

save(User('Tom', '123456'))
save(User('Jeck', 'pwd_abcd'))
save(User('Bob', 'bob456'))
print(db)

assert login('Tom', '123456')
assert login('Jeck', 'pwd_abcd')
assert not login('Bob', 'bad_password')
