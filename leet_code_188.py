#https://leetcode.com/problems/shuffle-string/
#Shuffle String
#You are given a string s and an integer array indices of the same length. 
#The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#Return the shuffled string.
#Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
#Output: "leetcode"
#Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
#Example 2:
#Input: s = "abc", indices = [0,1,2]
#Output: "abc"
#Explanation: After shuffling, each character remains in its position.

''.join(list(map(lambda n: n[0],sorted([(i,j) for i,j in zip(s,indices)],key=lambda n:n[1]))))