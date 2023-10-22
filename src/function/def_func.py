import math

# 函数的定义
def my_abs(n):
    if n >= 0:
        return n
    else:
        return -n

m = my_abs(-9)
print(m)


# 空函数
def nop():
    pass
# pass语句什么都不做
# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# my_abs('-1')

def my_abs_with_type_check(n):
    if not isinstance(n, (int, float)):
        raise TypeError('bad operand type')
    if n >= 0:
        return n
    else:
        return -n

# my_abs_with_type_check('-1')

# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r) # r 是一个tuple