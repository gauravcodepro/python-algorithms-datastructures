# Run lace or length algorithm
#given a string, convert into the run lace and the time of the storage
#for example, the given string is 
a='aaaabbbbbeeeessss'
#count the run lace
[list(map(lambda n: str(n) if type(n)==int else n,i)) 
                    for i in ([[i,a.count(i)] for i in set(list(a))])]
# final run lace 
''.join([j for i in ([list(map(lambda n: str(n) if type(n)==int else n,i)) 
                      for i in ([[i,a.count(i)] for i in set(list(a))])]) for j in i])
'e4a4s4b5'