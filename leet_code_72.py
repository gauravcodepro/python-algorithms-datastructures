#https://leetcode.com/problems/self-dividing-numbers/
#Self Dividing Numbers
#A self-dividing number is a number that is divisible by every digit it contains.
#For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#A self-dividing number is not allowed to contain the digit zero.
#Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
#Input: left = 1, right = 22
#Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
#Input: left = 47, right = 85
#Output: [48,55,66,77]
['True' if sum(list(filter(lambda n: len(n) > 1 and 0 not in n ,list(map(lambda n: [int(i) for i in n],
                   list(map(list,list(map(str,[i for i in range(1,100+1)]))))))))[i])%
                   list(filter(lambda n: len(n) > 1 and 0 not in n ,list(map(lambda n: [int(i) for i in n],
                   list(map(list,list(map(str,[i for i in range(1,100+1)]))))))))[i][0]==0 
                   and sum(a[i])%a[i][1] else 'False' for i in range(len(list(filter(lambda n: len(n) > 1 
                   and 0 not in n ,list(map(lambda n: [int(i) for i in n],
                   list(map(list,list(map(str,[i for i in range(1,100+1)]))))))))))]