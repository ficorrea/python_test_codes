import re

b = ['felipe', 'null', 'c0rr3a', '0123']

c = []
s = ''
for i in b:
    temp = re.findall(r'\d|null', i)
    if temp is None:
        c.append('x')
    else:
        c.append(s.join(temp))

print(c)