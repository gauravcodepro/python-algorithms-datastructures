#Combination Sum II (Medium)
#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations 
#in candidates where the candidate numbers sum to target.
#Each number in candidates may only be used once in the combination.
#Note: The solution set must not contain duplicate combinations.
#Example 1:
#Input: candidates = [10,1,2,7,6,1,5], target = 8
#Output: 
#[
#[1,1,6],
#[1,2,5],
#[1,7],
#[2,6]
#]
#Example 2:
#Input: candidates = [2,5,2,1,2], target = 5
#Output: 
#[
#[1,2,2],
#[5]
#]
####### filter based #############
from itertools import combinations
def f(val):
    return sum(val)==t
a = [10,1,2,7,6,1,5]
print(list(filter(f,list(combinations(a,3)))))
####### Comprehension based ##########
[i for i in (list(combinations(a,3))) if sum(i)==8]
######## list all the values #######
[(b-i) for i in a if (b-i) in a]
################################ using the zip 
list(zip(*[[i for i in (list(combinations(a,3))) if sum(i)==8],[i for i in (list(combinations(a,2))) if sum(i)==8]]))