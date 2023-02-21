#Rotate List(Medium)
#Given the head of a linked list, rotate the list to the right by k places.
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]
#Input: head = [0,1,2], k = 4
#Output: [2,0,1]
######
from collections import deque
head = [1,2,3,4,5]
k = 2
a=deque(head)
deque(['1', '2', '3', '4', '5'])
a.rotate(2)
print(a)
deque([4, 5, 1, 2, 3])
######
from collections import deque
head = [0,1,2]
k = 4
a=deque(head)
a.rotate(k)
print(a)
deque([2, 0, 1])