#https://leetcode.com/problems/super-palindromes/
#Super Palindromes
#Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.
#Given two positive integers left and right represented as strings, 
#return the number of super-palindromes integers in the inclusive range [left, right].
#Input: left = "4", right = "1000"
#Output: 4
#Explanation: 4, 9, 121, and 484 are superpalindromes.
#Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
[list(map(lambda n: [(i,'True') if i==i[::-1] else (i,'False') for i in n],
         (map(lambda n: [str(i)for i in n],[(i,i*i) for i in 
               ([i for i in range(2,1000)]) if i*i in [i for i in range(2,1000)]]))))]

[[('2', 'True'), ('4', 'True')],
 [('3', 'True'), ('9', 'True')],
 [('4', 'True'), ('16', 'False')],
 [('5', 'True'), ('25', 'False')],
 [('6', 'True'), ('36', 'False')],
 [('7', 'True'), ('49', 'False')],
 [('8', 'True'), ('64', 'False')],
 [('9', 'True'), ('81', 'False')],
 [('10', 'False'), ('100', 'False')],
 [('11', 'True'), ('121', 'True')],
 [('12', 'False'), ('144', 'False')],
 [('13', 'False'), ('169', 'False')],
 [('14', 'False'), ('196', 'False')],
 [('15', 'False'), ('225', 'False')],
 [('16', 'False'), ('256', 'False')],
 [('17', 'False'), ('289', 'False')],
 [('18', 'False'), ('324', 'False')],
 [('19', 'False'), ('361', 'False')],
 [('20', 'False'), ('400', 'False')],
 [('21', 'False'), ('441', 'False')],
 [('22', 'True'), ('484', 'True')],
 [('23', 'False'), ('529', 'False')],
 [('24', 'False'), ('576', 'False')],
 [('25', 'False'), ('625', 'False')],
 [('26', 'False'), ('676', 'True')],
 [('27', 'False'), ('729', 'False')],
 [('28', 'False'), ('784', 'False')],
 [('29', 'False'), ('841', 'False')],
 [('30', 'False'), ('900', 'False')],
 [('31', 'False'), ('961', 'False')]]
