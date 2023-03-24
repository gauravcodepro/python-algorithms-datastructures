#Reverse Vowels of a String
#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#Input: s = "hello"
#Output: "holle"
#Input: s = "leetcode"
#Output: "leotcede"
Concept: extract the vowel indices and splice and reverse it. 
Input: s = "hello"
Output: "holle"
[i for i in range(len(list(s))) if s[i] in list("aeiou")]
print(s[0]+s[1:][::-1])
[i for i in range(len(list(s))) if s[i] in list("aeiou")]
print(s[0]+s[1:][::-1])