# given any list, find the sum of the maximum values gap between consecutive elements
#leet code(Hard)
#Codewars
a = [3,6,9,1]
max([(b[i:i+2]) for i in range(len(sorted(b,key=lambda i:abs(i)))-(2-1))], key=lambda n: sum(n))
[6, 9]
The reason of using abs is that if the list contains the negative value then also it will work. 