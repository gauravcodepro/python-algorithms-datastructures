# Arthimetic progression
a= [1,3,5,7]
'True' if [abs(a[i]-a[i+1]) for i in range(len(a)-1)]==[abs(a[::-1][i]-a[::-1][i+1]) for i in range(len(a[::-1])-1)] else 'False'