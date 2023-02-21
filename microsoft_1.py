#Write code to search whether an array has a majority element. If yes, print it.
#Answer: The following C++ program searches for the majority element in an array 
#[10, 22, 22, 21, 22, 23, 22] and then prints it:
a=[10, 22, 22, 21, 22, 23, 22]
b=[]
from collections import Counter
for i in a:
    b.append((a.count(i),(i)))
print(b)
print(Counter(b).most_common(1))