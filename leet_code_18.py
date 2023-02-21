#calculate the euclidean distance of the data points in machine learning
#Euclidean distance = √Σ(Ai-Bi)2
from math import sqrt
a = [2, 4, 6, 8, 9, 10, 12, 15, 16, 24]
b = [4, 6, 6, 7, 8, 12, 14, 20, 23, 24]
sqrt(sum([pow((x-y),2) for x,y in zip(a,b)]))