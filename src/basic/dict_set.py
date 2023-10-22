#dict <=> map
# key的存放顺序和放入顺序无关

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# insert k-v
d['Krystal'] = 98
print(d['Krystal'])

d['Krystal'] = 96 # overwelm previous value
print(d['Krystal'])

# check if key is existed in dict
#1
hasVal = 'Amber' in d
print(hasVal)
#2
print(d.get('Amber') == None) # get None
print(d.get('Amber', -2) == -2) # get what you want


#delete an element
#1
d.pop('Bob')
print(d)


#set like dict is a list a keys, but no value,and no repeated key in it.
# and set is disordered.
s = set([1,2,3])
print(s)
s1 = set([1,2,3,5,6,7,2,1])
print(s1) # automaticly filter repated elements

#add element
s.add(4)
print(s)
# remove element
s.remove(2)
print(s)


# 不可变对象
# list是可变的
# str是不可变的
a = 'abc'
b = a.replace('a', 'A')#创建了一个新的字符串返回， 有些类似于golang中slice的扩容是会产生一个新的底层数组
print(a)
print(b)

