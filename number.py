numerator = int(input('Enter the numerator:'))
denominator = int(input('Enter the denominator:'))
if numerator == 0 :
     print(0)
     quit()
if numerator == denominator :
    print(1)
    quit()
if denominator == 0 or numerator < -2**31 or denominator > 2**31-1 :
    quit()
output = list()
if numerator < 0 or denominator < 0 :
    output.append('-')
numerator, denominator = abs(numerator), abs(denominator)
quotient = numerator // denominator
output.append(str(quotient))
remainder = numerator % denominator
if remainder == 0 :
    print(''.join(output))
output.append('.')
recurring_remainder = dict()
while remainder != 0 :
    if remainder in recurring_remainder :
        output.insert(recurring_remainder[remainder], '(')
        output.append(')')
        break
    recurring_remainder[remainder] = len(output)
    remainder *= 10
    output.append(str(remainder // denominator))
    remainder %= denominator
print(''.join(output))
