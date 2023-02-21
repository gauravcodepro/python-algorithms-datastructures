#Rearranging Digitshttps://www.interviewquery.com/questions/rearranging-digits
#Given a string n, a multi-digit number, write a function rearranging_digits to return a string of the smallest 
# number larger than n that can be created by rearranging the digits in n. Return None if no such number exists.
#Example:
#Input:
#n = '395'
#Output:
#def rearranging_digits(n) -> '539'#
n = '539'
[i for i in (''.join(i) for i in (list(permutations(sorted(n, key=lambda n: n[0]))))) if i[0] > i[1] and i[0] < max(i)]
number_of_permutations=
['539']
['359', '395', '539', '593', '935', '953']
n = '642'
[i for i in (''.join(i) for i in (list(permutations(sorted(n, key=lambda n: n[0]))))) if i[0] > i[1] and i[0] < max(i)]
number_of_permutations=['246', '264', '426', '462', '624', '642']
['426']