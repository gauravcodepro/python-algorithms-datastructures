#6 kyu https://www.codewars.com/kata/58ae6ae22c3aaafc58000079
#Permute a Palindrome
#DESCRIPTION: 
#Write a function that will check whether ANY permutation of the characters of the input string is a palindrome. 
# Bonus points for a solution that is efficient and/or that uses only built-in language functions. 
# Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.
#Example
#madam -> True
#adamm -> True
#junk -> False
#Hint
#The brute force approach would be to generate all the permutations of the string and check each one of them 
# whether it is a palindrome. However, an optimized approach will not require this at all.

from more_itertools import circular_shifts
from itertools import permutations
import polyleven
import stringtools.analysers

a='madam'
list(map(lambda n: ''.join(n),list(circular_shifts(a))))
print(list(map(lambda n: 'True' if is_palindrome(n) else 'False',list(map(lambda n: ''.join(n),list(circular_shifts(a)))))))
['madam', 'adamm', 'damma', 'ammad', 'mmada']
['True', 'False', 'False', 'False', 'False']

list(map(lambda n: ''.join(n),list(permutations(a))))
print(list(map(lambda n: 'True' if is_palindrome(n) else 'False',list(map(lambda n: ''.join(n),list(permutations(a)))))))

['madam', 'madma', 'maadm', 'maamd', 'mamda', 'mamad', 'mdaam', 'mdama', 'mdaam', 'mdama', 'mdmaa', 'mdmaa', 
'maadm', 'maamd', 'madam', 'madma', 'mamad', 'mamda', 'mmada', 'mmaad', 'mmdaa', 'mmdaa', 'mmaad', 'mmada', 
'amdam', 'amdma', 'amadm', 'amamd', 'ammda', 'ammad', 'admam', 'admma', 'adamm', 'adamm', 'admma', 'admam', 
'aamdm', 'aammd', 'aadmm', 'aadmm', 'aammd', 'aamdm', 'ammda', 'ammad', 'amdma', 'amdam', 'amamd', 'amadm', 
'dmaam', 'dmama', 'dmaam', 'dmama', 'dmmaa', 'dmmaa', 'damam', 'damma', 'daamm', 'daamm', 'damma', 'damam', 
'damam', 'damma', 'daamm', 'daamm', 'damma', 'damam', 'dmmaa', 'dmmaa', 'dmama', 'dmaam', 'dmama', 'dmaam', 
'amadm', 'amamd', 'amdam', 'amdma', 'ammad', 'ammda', 'aamdm', 'aammd', 'aadmm', 'aadmm', 'aammd', 'aamdm', 
'admam', 'admma', 'adamm', 'adamm', 'admma', 'admam', 'ammad', 'ammda', 'amamd', 'amadm', 'amdma', 'amdam', 
'mmada', 'mmaad', 'mmdaa', 'mmdaa', 'mmaad', 'mmada', 'mamda', 'mamad', 'madma', 'madam', 'maamd', 'maadm', 
'mdmaa', 'mdmaa', 'mdama', 'mdaam', 'mdama', 'mdaam', 'mamad', 'mamda', 'maamd', 'maadm', 'madma', 'madam']

['True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 
'False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 
'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 
'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False', 'False', 'False', 
'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 
'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 
'False', 'False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 
'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False', 
'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False', 'False', 
'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True']