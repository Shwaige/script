import uuid
import re

b = 10000
d = [1]
f = 0
for i in range(b):
    a = str(uuid.uuid4())
    c = re.search(r'\d', a) #获取uuid的第一位数字
    x = c.group()
    if int(x) in d:
        f = f + 1
    else:
        pass
    xx = f
print(xx)





