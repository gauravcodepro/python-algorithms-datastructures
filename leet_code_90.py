#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#Remove Duplicates from Sorted List
#Given the head of a sorted linked list, delete all duplicates such 
#that each element appears only once. Return the linked list sorted as well.
#Input: head = [1,1,2]
#Output: [1,2]
#Input: head = [1,1,2,3,3]
#Output: [1,2,3]

list(set(head))