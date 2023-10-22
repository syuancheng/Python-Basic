# python 有两种循环， 一种是for...in循环，依次把list或tuple中的每个元素迭代出来

fx = ['krystal', 'luna', 'amber', 'sulli', 'victoria']

for m in fx:
    print(m)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x

print(sum)

#如果list长度比较长， 不能都写出来，可以使用range函数来生成一个整数序列，然后通过list函数转为list

sum1 = 0
for x in range(101): #[0,101)
    sum1 = sum1 + x

print(sum1)


#while 
sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print(sum2)

# pritace
L = ['Bart', 'Lisa', 'Adam']
for n in L:
    print('Hello,', n, '!')