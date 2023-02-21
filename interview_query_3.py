#Alphabet Sum https://www.interviewquery.com/questions/alphabet-sum
#Given a list of strings of letters from a to z, create a function, sum_alphabet, that returns a list 
# of the alphabet sum of each word in the string.
#The alphabet sum is the sum of the ordinal position of each of the string’s letters in the standard 
# English alphabet ordering. So, the letter a will have a value of 1, z will have a value of 26, and so on.
#As an example of the alphabet sum of a string, the string sport will have an alphabet sum of 19 + 16 + 15 + 18 + 20 = 88.
#Example:
#Input:
#words = ["sport" , "good" , "bad"]
#Output:
#def sum_alphabet(words) -> [88 , 41 , 7]
if you have a single word
a="sport"       
   sum([(i[0]) for i in [(n,c) for n,c in enumerate((chr(c+65).lower() 
                                 for c in range(26)),1)] for j in list(a) if j in i])
88
if you have a nested word list
words = ["sport" , "good" , "bad"]
   sum([(i[0]) for i in [(n,c) for n,c in enumerate((chr(c+65).lower() 
                           for c in range(26)),1)] for j in list(words) for k in j if k in i])
136
words = ["sport" , "good" , "bad"]
[(sum([(i[0]) for i in [(n,c) for n,c in enumerate((chr(c+65).lower() 
                           for c in range(26)),1)] for j in list(n) if j in i])) for n in words]
[88 , 41 , 7]