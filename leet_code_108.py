#https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
#Decrypt String from Alphabet to Integer Mapping
#You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
#Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
#Return the string formed after mapping.
#The test cases are generated so that a unique mapping will always exist.
#Input: s = "10#11#12"
#Output: "jkab"
#Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
#Input: s = "1326#"
#Output: "acz"

first find the indices and since it it a three character 
so take the string before and after the indices
[s.find(i) for i in re.findall(r'[0-9][0-9]{,1}[#]',s)]
[0, 3]
mapping_index=list(map(int,[i.replace('#','') for i in (list(re.findall(r'[0-9][0-9]{,1}[#]',s))+list(s[6:]))]))
[10, 11, 1, 2]
character_list= ''.join([i[1] for i in ([j for i in ([[i] for i in [(i,id) for i,id in enumerate([chr(i+97) 
   for i in range(26)],1)] if 10 in i]+[[i] for i in [(i,id) for i,id in enumerate([chr(i+97) 
    for i in range(26)],1)] if 11 in i]+[[i] for i in [(i,id) for i,id in enumerate([chr(i+97) 
     for i in range(26)],1)] if 1 in i]+[[i] for i in [(i,id) for i,id in enumerate([chr(i+97) 
      for i in range(26)],1)] if 2 in i]) for j in i])])