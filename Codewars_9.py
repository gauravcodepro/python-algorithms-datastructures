#Codewars
#Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
#balancedParens 0 -> [""]
#balancedParens 1 -> ["()"]
#balancedParens 2 -> ["()()","(())"]
#balancedParens 3 -> ["()()()","(())()","()(())","(()())","((()))"]
first approach 
from itertools import permutations
def balancedParens(n):
    return [list(map(lambda n: ''.join(n),list(permutations(n))))]
second approach 
def balancedParens(n):
    return [list(map(lambda n: ''.join(n),list(combinations(n))))]