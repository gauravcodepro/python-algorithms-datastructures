# Top interview question
# given a list, convert into a single alphabet for encoding.
a=[[86, 81, 74, 67, 85, 83, 72, 65, 69, 71, 78, 90],[87, 82, 80, 89, 70, 84, 76, 68, 75, 73, 77, 79, 88, 66]]
from functools import reduce
[chr(j) for j in ((reduce(lambda a,b : a+b,v)) for v in (list(map(lambda n:n*2,m)) for m in (list(filter(lambda n: n%2==1,i)) for i in a)))]
['В', 'π']