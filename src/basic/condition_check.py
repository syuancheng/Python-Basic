age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')

#当我们用if ... elif ... elif ... else ...判断时，会写很长一串代码，可读性较差。
#如果要针对某个变量匹配若干种情况，可以使用match语句。
score = 'B'
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _:
        print('score is ???')
