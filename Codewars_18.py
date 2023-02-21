# range compression 
# you are given a list of the ints and compress the range according to
# the int range difference
# i applied the int to string and then used the string interpolation
a=[10,20,40,30,50]
# loop based
for j in range(len(a)):
    for i in range(len(a)-j-1):
        if a[j]-a[j+1]==10:
            print((str(a[i])+'-'+str(a[i+1])))