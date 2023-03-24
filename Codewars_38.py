# https://www.codewars.com/kata/5679aa472b8f57fb8c000047
# You are going to be given an array of integers. Your job is to take that array and find an index N where the
# sum of the integers to the left of N is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.
# For example:
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left
# side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array, the sum of left side
# of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.
# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N.
# If you do not find an index that fits these rules, then you will return -1
concept: caling the range starting at the second element as the range will be null for 0 and 1 for the zero division error
and then using that range to create list partitions and now you can map the sum or the divide or reduce anything on this.

[(a[:len(a)//i], a[len(a)//i:][0], a[len(a)//i:][1:])
 for i in range(2, len(a))]

[([1, 2, 3], 4, [3, 2, 1]),
 ([1, 2], 3, [4, 3, 2, 1]),
 ([1], 2, [3, 4, 3, 2, 1]),
 ([1], 2, [3, 4, 3, 2, 1]),
 ([1], 2, [3, 4, 3, 2, 1])]
