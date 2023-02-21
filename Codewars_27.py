'''
calculating the char frequency in the text
'''
a=transpose a matrix according to the indexes and then sort the matrix 
from collections import Counter
print(Counter([j for i in (list(map(lambda n: list(n),a.split()))) for j in i]))
Counter({'t': 8, 'a': 6, 'e': 6, 'r': 5, 'n': 5, 's': 4, 'o': 4, 'i': 4, 
         'x': 3, 'd': 3, 'h': 3, 'm': 2, 'c': 2, 'p': 1, 'g': 1})
print(dict([(i,[j for i in (list(map(lambda n: list(n),a.split()))) for j in i].count(i)) for i in 
      ([j for i in (list(map(lambda n: list(n),a.split()))) for j in i])]))
{'t': 8, 'a': 6, 'e': 6, 'r': 5, 'n': 5, 's': 4, 'o': 4, 'i': 4, 
         'x': 3, 'd': 3, 'h': 3, 'm': 2, 'c': 2, 'p': 1, 'g': 1}