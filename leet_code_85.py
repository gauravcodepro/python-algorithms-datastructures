#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
#Number of Substrings Containing All Three Characters
#Given a string s consisting only of characters a, b and c.
#Return the number of substrings containing at least one occurrence of all these characters a, b and c.
#Input: s = "abcabc"
#Output: 10
#Explanation: The substrings containing at least one occurrence of the characters 
#a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" 
#Input: s = "aaacb"
#Output: 3
#Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
list(filter(lambda n: 'a' in n and 'b' in n and 'c' in n,(filter(lambda n: n!='',
       ((set([s[:i:[i for i in range(1,len(s)+1)][j]]for i in range(len(s)) 
             for j in range(len([i for i in range(1,len(s)+1)]))]+[s[i:i+[i 
                 for i in range(1,len(s)+1)][j]]for i in range(len(s)) for j in range(len
                 ([i for i in range(1,len(s)+1)]))]+[s[:[i for i in range(1,len(s)+1)][j]]
                 for i in range(len(s)) for j in range(len([i for i in range(1,len(s)+1)]))]+
                 [s[i:i+[i for i in range(1,len(s)+1)][j]]for i in range(len(s)) 
                 for j in range(len([i for i in range(1,len(s)+1)]))])))))))