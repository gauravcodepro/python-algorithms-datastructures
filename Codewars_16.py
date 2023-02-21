#https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9
#Make two comprehensions like one with the even and one with the odd.
# See below i am using the enumerate and then using the enumerate id to index 
# the odd and the even out and then summing them.
a=[13, 27, 49]
sum([id for i,id in enumerate(a,1) if i%2==0]),sum([id for i,id in enumerate(a,1) if i%2==1])
(27, 62)