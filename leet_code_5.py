#Sum of two values
#Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. 
#Return true if the sum exists and return false if it does not.
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
a = [2, 7, 11, 15]
b = 9
[(b-n) for n in a if b-n in a]