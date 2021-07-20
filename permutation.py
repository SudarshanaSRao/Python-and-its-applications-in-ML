x = float(input('Enter the base:'))
n = int(input('Enter the exponent:'))
if x<-100.0 or x>100.0 :
    if n<2**-31 or n>2**31-1 :
        quit()
if pow(x,n)<-10**4 or pow(x,n)>10**4 :
    quit()
else :
    print(pow(x,n))
#Program to print out permutation sequence
from itertools import permutations
n=int(input('Enter a number:'))
k=int(input('Enter the digit limit:'))
list1 = [str(i) for i in range(1, n+1)]
list1 = "".join(list1)
list2 = sorted(list(permutations(list1, n)))
print("".join(list2[k-1]))
