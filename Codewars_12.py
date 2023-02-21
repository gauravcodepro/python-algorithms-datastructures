#given a list, sort the list according to the bin size
#Codewars
a = [3,6,9,1]
#function approach
def bin_sort(a):
    for i in range(len(a)-1):
        if bin(a[i]) < bin(a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
        return a
bin_sort(a)
[6, 3, 9, 1]