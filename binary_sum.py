a = input("Enter the first number:")
b = input("Enter the second number:")
if len(a)<1 or len(b)>10**4:
    quit()
if a[0] == '0' or b[0] == '0' :
    print("The number shouldn't start with a leading zero")
    quit()
try :
    A = int(a, 2)
    B = int(b, 2)
except :
    print('Enter the numbers with digit containing only 0 or 1')
    quit()
C = A + B
C = bin(C)
print(C[2:])
