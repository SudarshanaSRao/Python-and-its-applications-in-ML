# Program to find the quotient of two numbers without using the division operation.
dividend=int(input('dividend='))
divisor=int(input('divisor='))
if dividend<-2**31 or divisor>2**31-1 or divisor==0:
    quit()
sign=-1 if ((dividend<0) or (divisor<0)) else 1
quotient=0
dividend=abs(dividend)
divisor=abs(divisor)
while dividend>=divisor:
    dividend-=divisor
    quotient+=1
print(sign*quotient)
if quotient>2**31-1:
    print(2**31-1)

#Program to check if  number is palindrome or not.
num=int(input('Enter a number:'))
y=num
d=0
while num>0:
    a=num%10
    num=num//10
    d=d*10+a
if d==y:
    print('The number is palindome')
else:
    print('The number is not palindrome')
