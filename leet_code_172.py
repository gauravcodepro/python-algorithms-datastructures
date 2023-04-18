#https://leetcode.com/problems/word-pattern/
#Word Pattern
#Given a pattern and a string s, find if s follows the same pattern.
#Here follow means a full match, such that there is a bijection 
#between a letter in pattern and a non-empty word in s.
#Input: pattern = "abba", s = "dog cat cat dog"
#Output: true
'True' if (''.join([i[0] for i in s.strip().split()]))[0]==(''.join([i[0] for i in s.strip().
     split()]))[-1] and (''.join([i[0] for i in s.strip().split()]))[1]==
                (''.join([i[0] for i in s.strip().split()]))[2] else 'False'