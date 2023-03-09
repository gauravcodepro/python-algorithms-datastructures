#https://leetcode.com/problems/zigzag-conversion/
#The string "PAYPALISHIRING" is written in a zigzag pattern 
#on a given number of rows like this: 
#(you may want to display this pattern in a 
#fixed font for better legibility)
#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#Write the code that will take a string and make 
#this conversion given a number of rows:
#string convert(string s, int numRows);
#Example 1:
#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"
#Example 2:
#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I
#Example 3:
#Input: s = "A", numRows = 1
#Output: "A"
s=str(input('Enter a string with spaces:')):
return ''.join([j for i in (list(filter(lambda n: n!=[''],[list(map(lambda n: n.replace(' ',''),i)) 
                           for i in (''.join(a.split('\n')))]))) for j in i])

New solution

''.join(list(map(lambda n:n.replace(' ', ''),(re.split(r'\n+',a)))))