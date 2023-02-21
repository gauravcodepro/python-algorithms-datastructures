#Move Zeros Back # https://www.interviewquery.com/
#Given an array of integers, write a function move_zeros_back that moves all zeros in the array to the end of the array. 
# If there are no zeros, return the input array.
Example:
Input:
#array = [0,5,4,2,0,3]
#def move_zeros_back(array) -> [5,4,2,3,0,0]
first approach = 
list(reversed(sorted(a, key=lambda n: n>0 and -n)[::-1]))
[5, 4, 3, 2, 0, 0]
second approach
[j for i in ([i for i in a if i>0], [i for i in a if i==0]) for j in i]