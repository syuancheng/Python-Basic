import re

string = "123abc"
pattern = r'\d+'  # 匹配一个或多个数字

match = re.match(pattern, string)

if match:
    print("匹配成功")
else:
    print("匹配失败")


t = re.match(r'(.*)T(.*):(.*):(.*)Z', "2024-03-19T18:00:00Z", re.I)
k = t.group(2)
print(t)
print(k)
