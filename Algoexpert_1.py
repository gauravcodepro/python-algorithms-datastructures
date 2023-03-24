https://www.algoexpert.io/questions/validate-subsequence
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print([(i,'True') if i in sequence else 'False' for i in array])
['False', (1, 'True'), 'False', 'False', (6, 'True'), (-1, 'True'), 'False', (10, 'True')]
[list(map(lambda n: 'True' if i==j else 'False',i) for i in sequence for j in array)]