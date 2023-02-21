# leet code question(hard)
# list comprehension way of calculating the canberra distance
# Canberra distance = Σ |Ai-Bi| / (|Ai| + |Bi|)
a = [2, 4, 4, 6, 8, 10]
b = [5, 5, 7, 8, 10, 12]
sum([abs(x-y)/abs(x+y) for x, y in zip(a, b)])