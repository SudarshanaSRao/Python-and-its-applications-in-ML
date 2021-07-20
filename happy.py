n = int(input('Enter a number:'))
s = set()
while True :
    if n!= 1 :
        if n not in s :
            s.add(n)
            n = str(n)
            cnt = 0
            for i in n :
                cnt += int(i) * int(i)
            n = cnt
        else :
            print(False)
            break
    else :
        print(True)
        break
