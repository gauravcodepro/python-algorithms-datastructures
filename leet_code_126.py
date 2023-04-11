#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#Find Minimum in Rotated Sorted Array
#Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
#For example, the array nums = [0,1,2,4,5,6,7] might become:
#[4,5,6,7,0,1,2] if it was rotated 4 times.
#[0,1,2,4,5,6,7] if it was rotated 7 times.
#Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 
# 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#You must write an algorithm that runs in O(log n) time.
#Input: nums = [3,4,5,1,2]
#Output: 1
#Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#Input: nums = [4,5,6,7,0,1,2]
#Output: 0
#Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
#Input: nums = [11,13,15,17]
#Output: 11
#Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

def insertionSort(list):
   for i in range(1,len(list)):
       place_holder = list[i]
       while i>0 and list[i-1]>place_holder:
           list[i] = list[i-1]
           i = i-1
           list[i] = place_holder
   return list
print(insertionSort([5,2,1,9,0,4,6])[:1])

#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
#Find Minimum in Rotated Sorted Array II
#Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
#For example, the array nums = [0,1,4,4,5,6,7] might become:
#[4,5,6,7,0,1,4] if it was rotated 4 times.
#[0,1,4,4,5,6,7] if it was rotated 7 times.
#Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
#results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
#You must decrease the overall operation steps as much as possible.
#Input: nums = [1,3,5]
#Output: 1
#Example 2:
#Input: nums = [2,2,2,0,1]
#Output: 0

def insertionSort(list):
   for i in range(1,len(list)):
       place_holder = list[i]
       while i>0 and list[i-1]>place_holder:
           list[i] = list[i-1]
           i = i-1
           list[i] = place_holder
   return list
print(insertionSort([5,2,1,9,0,4,6])[:1])

