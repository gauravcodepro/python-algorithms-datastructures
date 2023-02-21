#compress the range without using the backtracking
a=[0, 2, 4, 5, 7, 8, 9]
for i in range(len(a)-1):
    if abs(a[i]-a[i+1])==2:
        print(str(a[i])+'-'+str(a[i+1]))
    elif abs(a[i]-a[i+1])==1:
            print(str(a[i])+'-'+str(a[i+1]))
0-2
2-4
4-5
5-7
7-8
8-9