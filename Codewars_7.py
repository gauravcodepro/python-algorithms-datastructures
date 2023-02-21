#6 kyu https://www.codewars.com/kata/541c8630095125aba6000c00
#Sum of Digits / Digital Root
#DESCRIPTION:
#Digital root is the recursive sum of all the digits in a number.
#Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#Examples
#    16  -->  1 + 6 = 7
#   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
#first approach
a=132189
# first apply an accumulate and the last element will be the sum of all
list(accumulate(map(lambda n: int(n),list(str(a))),lambda x,y:x+y)) 
[1, 4, 6, 7, 15, 24]
# take the last element and then sum it.
sum(map(lambda n: int(n),list(str(list(accumulate(map(lambda n: int(n),list(str(a))),lambda x,y:x+y))[-1]))))
# second approach 
int(sum(map(lambda n: int(n,list(str(a))))))
# third approach 
from functools import reduce
def add(x,y):
    return(x+y)
reduce(add,map(int,list(str(reduce(add,list(map(lambda n: int(n),list(str(a)))))))))