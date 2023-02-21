#Super Palindromes(Hard)
#Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.
#Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].
#Example 1:
#Input: left = "4", right = "1000"
#Output: 4
#Explanation: 4, 9, 121, and 484 are superpalindromes.
#Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
#Example 2:
#Input: left = "1", right = "2"
#Output: 1
import polyleven
from stringtools.analysers import *
[(i,i*i) for i in ([i for i in range(1,1000,1)]) if is_palindrome(i) and is_palindrome(i*i)]
[(1, 1), (2, 4), (3, 9), (11, 121), (22, 484), (101, 10201), (111, 12321), (121, 14641), (202, 40804),(212, 44944)]
### only the i
[i for i in ([i for i in range(1,1000,1)]) if is_palindrome(i) and is_palindrome(i*i)]
[1, 2, 3, 11, 22, 101, 111, 121, 202, 212]