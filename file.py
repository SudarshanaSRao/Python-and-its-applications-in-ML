import re
fname=open('abstract.txt')
lst=list()
s=0
for line in fname:
    number=re.findall('[0-9]+',line)
    lst=lst+number
for z in lst:
    s+=int(z)
print(s)
