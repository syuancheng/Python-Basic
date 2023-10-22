# list

classmates = ['krystal', 'luna', 'amber', 'suli']

# append 追加元素到末尾
classmates.append('virtory')

# 加入元素到指定位置
classmates.insert(1, 'jessica')

# len() get elements count
print(classmates, len(classmates))
print(classmates[-1])

# 删除末尾元素
classmates.pop()
print(classmates, len(classmates))

# 删除指定位置元素
classmates.pop(1)

l = ['sheli', 'tim', 123, True]
print(l)

# 替换某个元素
classmates[1] = 'krystal'

# list中的元素可以是不同类型
p = ['go']
s = ['jave', 'python', p, 'c++']
print(p[0] == s[2][0])

# 空的list， len=0
emptyL = []
print(len(emptyL))


# tuple， 和list相似，但是一旦初始化就不能修改了
# 不支持append insert 和赋值
# why？ 因为tuple不可变， 所以更安全， 能用tuple代替list就尽量用tuple
roommates = ('Michael', 'Bob', 'Tracy')

#空
t = ()
# 一个元素
s = (1,)

# 可变的tuple
r = ('a', 'b', ['A', 'B'])
r[2][0] = 'X'
r[2][1] = 'Y'
print(r)