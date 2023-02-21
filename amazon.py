# Amazon Top interview question
# List only those numbers whose parity for data storage and computation is 1.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(None,[list(filter(lambda x: x%2==0,list(map(int,(bin(i)[2:],i))))) for i in a]))
[[10, 2], [100, 4], [110, 6], [1000, 8], [1010, 10]]