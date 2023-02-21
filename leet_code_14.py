#Reverse Nodes in k-Group(Hard)
#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# Define node point is a even node junction. For odd i already posted result earlier.
#You may not alter the values in the list's nodes, only nodes themselves may be changed.
#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]
from more_itertools import chunked
head = [1,2,3,4,5]
list((i[::-1] if len(i)>=2 else i for i in (list(chunked(head,2)))))