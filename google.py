#String segmentation
#You are given a dictionary of words and a large input string. You have to find out whether the input string can be completely 
#segmented into the words of a given dictionary. The following two examples elaborate on the problem further.
#Input: s = "applepenapple", wordDict = ["apple", "pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             #Note that you are allowed to reuse a dictionary word.
from more_itertools import windowed
s = "applepenapple"
wordDict = ["apple", "pen"]
b=(list(windowed(list(s),3)))
dictionary=[]
for i in b:
    dictionary.append(''.join(i))
print(dictionary)
for i in dictionary:
    for j in wordDict:
        if i==j:
            print(any(i))

#Largest sum subarray
#In the array below, the largest sum subarray starts at index 3 and ends at 6, and with the largest sum being 12.
#Input: [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.
from more_itertools import windowed
print([i for i in list(windowed(a,4))]) 
print([sum(i) >= 6 for i in list(windowed(a,4))])


# Google top question number 4
4. Delete node with a given key
#We are given the head of a linked list and a key. We have to delete the node that contains this given key. 
# The following two examples elaborate on this problem further.
Input: head = [4,5,1,9], key = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
print(list(filter(lambda i: i!=key,head)))