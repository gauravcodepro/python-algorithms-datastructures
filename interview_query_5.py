#Sliding Window Median(Hard)
#The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. 
# So the median is the mean of the two middle values.
#For examples, if arr = [2,3,4], the median is 3.
#For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
#You are given an integer array nums and an integer k. There is a sliding window of size k which is moving 
# from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
#Example 1:

#Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
#Explanation: 
#Window position                Median
#---------------                -----
#[1  3  -1] -3  5  3  6  7        1
# 1 [3  -1  -3] 5  3  6  7       -1
# 1  3 [-1  -3  5] 3  6  7       -1
# 1  3  -1 [-3  5  3] 6  7        3
# 1  3  -1  -3 [5  3  6] 7        5
# 1  3  -1  -3  5 [3  6  7]       6
#Example 2:
#Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
#Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

# Arthimetic median for arrays when the arrays are even
a=[1, 2, 3, 4, 5, 6, 2, 5, 7, 8, 3, 9, 10, 12, 0, 1, 2, 8]
n=len(a)//2
[sum(i)/2 for i in ((i[0][-1],i[1][0]) 
            for i in ((i[:n],i[n:]) for i in [sorted(a)]))]

# Arthimetic median for list of lists when the lists are even
a=[[1, 2, 3, 4, 5, 6, 2, 5, 7, 8, 3, 9, 10, 12, 0, 1, 2, 8],[24,36,30,15,17,18,25,36],[20,17,19,18,12,16,10,4,6,3]]
n=[len(i)//2 for in a]
[[sum(i)/2 for i in ((i[0][-1],i[1][0]) 
                for i in ((i[:n],i[n:]) for i in [sorted(i)]))] for i in a]

#Arthmetic median when the arrays are odd
a=[15, 6, 16, 8, 22, 21, 9, 18, 25]
[print(i,id) for i,id in enumerate(sorted(a),1) 
                        if (int((len(sorted(a))+1)//2))==i]
# Arthmetic median for the sliding windows arrays when it is odd 
from more_itertools import windowed
nums = [1,3,-1,-3,5,3,6,7]
[(1, 3, -1), (3, -1, -3), (-1, -3, 5), (-3, 5, 3), (5, 3, 6), (3, 6, 7)]
[print(i,id) for i,id in enumerate(sorted(a),1) 
                        if (int((len(sorted(a))+1)//2))==i] # iterate this over all the windows