#https://leetcode.com/problems/sort-an-array/
#Given an array of integers nums, sort the array in ascending order and return it.
#You must solve the problem without using any built-in functions in O(nlog(n)) time 
#complexity and with the smallest space complexity possible.
#Input: nums = [5,2,3,1]
#Output: [1,2,3,5]
#Explanation: After sorting the array, the positions of some numbers are not changed
#(for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
#Input: nums = [5,1,1,2,0,0]
#Output: [0,0,1,1,2,5]
#Explanation: Note that the values of nums are not necessairly unique.
# Simple sorting
sorted(arr)
[1, 2, 3, 5]
#bin wise sorting
sorted(arr, key=lambda i: bin(i))
[1, 2, 3, 5]
# using the insertion sort
def sortInsert(arr):
    for i in range(1,len(arr)):
        place=arr[i]
        while i>0 and arr[i-1]> place:
            arr[i]=arr[i-1]
            i=i-1
            arr[i]=place
            return arr