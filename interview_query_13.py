#https://www.interviewquery.com/questions/summing-numeric-strings
#Summing Numeric Strings
#Given two strings, num_str1 and num_str2, write a function to sum the two strings together without directly converting them to integers.
#Note: Return the output in string format.
#Example:
#Input:
#num_ str1 = '122' #assume that in practice the two strings are huge
#num_str2 = '222'
#Output:sum_strings(num_str1,num_str2) -> '344'
n1=122
n2=222
sum(list(map(lambda n: ord(n),list((chr(n1)+chr(n2))))))
sum=344
n1=567
n2=687
sum(list(map(lambda n: ord(n),list((chr(n1)+chr(n2))))))
1254