#!/usr/bin/env python3


msg = "Roll a dice"
print(msg, "test")

print('12 + 14 =', 26)

# name = input()
# print(name)


# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(s4)

classmates = ['krystal', 'luna', 'amber', 'suli']
classmates.append('virtory')
classmates.insert(1, 'jessica')
print(classmates, len(classmates))
print(classmates[-1])

classmates.pop()
print(classmates, len(classmates))

l = ['sheli', 'tim', 123, True]
print(l)


p = ['go']
s = ['jave', 'python', p, 'c++']
print(p[0] == s[2][0])


emptyL = []
print(len(emptyL))