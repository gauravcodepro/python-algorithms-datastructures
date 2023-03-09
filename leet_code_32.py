#Merge k Sorted Lists (Hard) Leet code
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.
#Example 1:
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
# 1->3->4,
# 2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6 
#passing all the nested lists as positional arguments and then filtering None, dont 
#use zip as it will exhaust when the iterable length differs instead  put the zip_longest
from itertools import zip_longest
sorted([j for i in [list(filter(None,i)) for i in ([list(l) for l in zip_longest(*lists)])] for j in i])
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
# if you have to write the function then it would be to call the range(len(lists)) and within the lists
#call the range(len(list)) so a nested range. 
# now if the questions becomes according to the bin sorting of the linked list then the code becomes
sorted([j for i in [list(filter(None,i)) for i in ([list(l) for l in zip_longest(*lists)])] for j in i],key=lambda i: bin(i))
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]