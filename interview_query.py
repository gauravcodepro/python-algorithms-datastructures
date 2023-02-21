# calculate the iterative sum of the windows of the given list in a single line
# Google interview question
a=[20,17,19,18,12,16,10,4,6,3]
print([(a[i:i+2]) for i in range(len(a) - (2-1))])
#[[20, 17], [17, 19], [19, 18], [18, 12], [12, 16], [16, 10], [10, 4], [4, 6], [6, 3]]
[sum((a[i:i+2])) for i in range(len(a) - (2-1))]
#[37, 36, 37, 30, 28, 26, 14, 10, 9]