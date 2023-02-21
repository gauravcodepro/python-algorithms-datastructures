# implement a count without using the counter from collections
s='AAABCCDDDD'
sorted([(i,s.count(i)) for i in set(list(s))])
[('A', 3), ('B', 1), ('C', 2), ('D', 4)]