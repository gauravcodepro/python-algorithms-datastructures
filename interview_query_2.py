#Check Matching Parentheses https://www.interviewquery.com/questions/check-matching-parentheses
#One of the basic steps in parsing string inputs is to check whether the opening and closing characters or tags match, 
# i.e., to check if each opened parenthesis is closed eventually.
#Given a list of strings, write a string parser that verifies the integrity of the parenthesis used in the string. 
# The parser should return a list of booleans stating whether that string’s integrity was verified.
#Example:
#Input:
#list_of_strings = [
#    'f(x) + g(x)', 
#    'sin(exp(x)}', 
#    '((())just some string)', 
#    '(4,{(3,4):x**2)']
To count all the matching strings and make a tuple
[(i.count('()'), i.count('('), i.count(')')) for i in list_of_strings]
[(0, 2, 2), (0, 2, 1), (1, 3, 3), (0, 2, 2)]
[print(i,'matching_pattern') for i in list_of_strings if (i.count('()')+i.count('(')+i.count(')'))%2==0]
f(x) + g(x) matching_pattern
(4,{(3,4):x**2) matching_pattern