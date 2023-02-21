#Codewars, leetcode
#Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
#balancedParens 0 -> [""]
#balancedParens 1 -> ["()"]
#balancedParens 2 -> ["()()","(())"]
#balancedParens 3 -> ["()()()","(())()","()(())","(()())","((()))"]
print([i for i in (list(map(lambda n: ''.join(n),list(permutations(s))))) if i.startswith('(') and i.endswith(')')]) 
['(())', '(())', '()()', '()()', '(())', '(())', '()()', '()()']
print(set([i for i in (list(map(lambda n: ''.join(n),list(permutations(s))))) if i.startswith('(') and i.endswith(')')])) 
{'()()', '(())'} # made a set for all the unique combinations