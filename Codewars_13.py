#6 kyu https://www.codewars.com/kata/58039f8efca342e4f0000023
#DESCRIPTION:
#Create a function that takes a string as a parameter and does the following, in this order:
#Replaces every letter with the letter following it in the alphabet (see note below)
#Makes any vowels capital
#Makes any consonants lower case
#Note:
#the alphabet should wrap around, so Z becomes A
# in this kata, y isn't considered as a vowel.
# So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)
#first approach using simple comprehension
a="Cat30" 
''.join([chr(ord(i)-32) if i in 'aeiou' else i for i in ([chr(ord(i)+1).lower() 
                                                for i in a if i.isalpha()]+[i for i in a if i.isdigit()])])
#second approach using the map
''.join(list(map(lambda n: chr(ord(n)-32) if n in 'aeiou' else n,(map(lambda n: 
                    chr(ord(n)+1).lower(),[i for i in a if i.isalpha()]))))+[i for i in a if i.isdigit()])