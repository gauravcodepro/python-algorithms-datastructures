#Reverse Nodes in k-odd Group (Hard)
#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#k is a positive integer and is less than or equal to the length of the linked list.
#You may not alter the values in the list's nodes, only nodes themselves may be changed.
#Example 1:
#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]
head = [1,2,3,4,5,6,7,8,9,10]
k = 3
from more_itertools import split_after
[list(merge(*(i[::-1] if k in i else i for i in (list(split_after(head,lambda num: num==k))))))]
[[3, 2, 1, 4, 5, 6, 7, 8, 9, 10]]
head = [1,2,3,4,5]
k = 3
from more_itertools import split_after
[list(merge(*(i[::-1] if k in i else i for i in (list(split_after(head,lambda num: num==k))))))]
[[3, 2, 1, 4, 5]]
See in this i am not using the .chain as .chain loads the list into memory. Instead using the merge which is almost no memory. 