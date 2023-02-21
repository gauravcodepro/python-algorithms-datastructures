#Reverse Words in a Sentence Amazon question
from collections import deque
a = ['Hello','World']
b=deque(['Hello','World'])
b.rotate(-1)
print(b)
deque(['World', 'Hello'])