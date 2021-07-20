my_bin=input('Enter binary to be converted:')
n=len(my_bin)
print(n)
res=0
for i in range(1,n+1):
    res=res+int(my_bin[i-1])*2**(n-i)
print ("The decimal of the given binary is",res,'.')

#Program to reverse a number.
x=int(input('Enter a number:'))
dig=0
while x>0:
    n=x%10
    x=x//10
    dig=dig*10+n
print(dig)
