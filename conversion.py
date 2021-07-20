#Program to find the pig latin of a word
word = "trouble"
ans = ""
for x in word :
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" :
        ans+=x
        break
c = word.split(ans)
ans+=c[1]
ans+=c[0]
ans+="ay"
print(ans)
#Program to convert string into integer
str=input('Enter a string:')
intval = 0
try :
    intval = int(str)
except :
    str = str.strip()
    nums = 0
    coms = 0
    for index,ele in enumerate(str):
        if (ele == '-' or ele == '+') and coms == 0 :
            nums+=1
        elif ele not in ('0','1','2','3','4','5','6','7','8','9') or nums>1 :
            try :
                intval = int(str[:index])
                break
            except :
                intval = 0
                break
            else :
                coms+=1
if intval<=-2**31 :
    print(-2**31)
elif intval>=2**31-1 :
    print(2**31-1)
else :
    print(intval)
