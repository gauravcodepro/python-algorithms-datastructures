# https://leetcode.com/problems/remove-invalid-parentheses/(Hard)
# Remove Invalid Parentheses
# Given a string s that contains parentheses and letters, remove the minimum number
# of invalid parentheses to make the input string valid.
# Return a list of unique strings that are valid with the minimum number of
# removals. You may return the answer in any order.
s = "()())()"
s.count("(")
s.count(")")
[str(a[i])+str(b[i]) for i in range(len(b)-1)]
['()', '()', '()']
Concept count the bracket in the first orientation,
count the bracket in the second orientation and then which is higher less the range
and then simply add the less range to the other. Simple solution
