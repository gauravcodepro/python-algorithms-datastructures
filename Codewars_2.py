# Codewars decoding 
#You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
#For each word:
#the second and the last letter is switched (e.g. Hello becomes Holle)
#the first letter is replaced by its character code (e.g. H becomes 72)
#Note: there are no special characters used, only letters and spaces
#Examples
#decipherThis('72olle 103doo 100ya'); // 'Hello good day'
#decipherThis('82yade 115te 103o'); // 'Ready set go'
from itertools import permutations
a='72olle 103doo 100ya'
a=list(a.split())
[list(map(lambda n: ''.join(n),i)) for i in [list(permutations(i)) for i in 
    [(chr(int(a[0][:2]))+a[0][2:]),(chr(int(a[1][:3]))+a[1][3:]),(chr(int(a[2][:3]))+a[2][3:])]]]

##### 
from itertools import permutations
a='72olle'
b=[]
c=[]
for i in list(a):
    if i in ([i.lower() for i in {chr(c+65) for c in range(26)}]):
        b.append(i)
    if i not in [i.lower() for i in {chr(c+65) for c in range(26)}]:
        c.append(i)
        (''.join([chr(int((''.join(c)))),''.join(b)]))
[i for i in [''.join(i) for i in(list(permutations((''.join([chr(int((''.join(c)))),''.join(b)])))))] if i.startswith('H')]
['Holle', 'Holel', 'Holle', 'Holel', 'Hoell', 'Hoell', 'Hlole', 'Hloel', 'Hlloe', 'Hlleo', 'Hleol', 'Hlelo', 'Hlole', 'Hloel', 
'Hlloe', 'Hlleo', 'Hleol', 'Hlelo', 'Heoll', 'Heoll', 'Helol', 'Hello', 'Helol', 'Hello']