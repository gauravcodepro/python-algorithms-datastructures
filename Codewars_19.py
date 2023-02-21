#write a program to calculate the Armstrong number
a=153
print('Amstrong Number') if sum([i**3 for i in list(map(lambda n: int(n),list(str(a))))]) == a else print('No Amstrong Number')
Amstrong Number
a=371
print('Amstrong Number') if sum([i**3 for i in list(map(lambda n: int(n),list(str(a))))]) == a else print('No Amstrong Number')
Amstrong Number
a=261
print('Amstrong Number') if sum([i**3 for i in list(map(lambda n: int(n),list(str(a))))]) == a else print('No Amstrong Number')
No Amstrong Number