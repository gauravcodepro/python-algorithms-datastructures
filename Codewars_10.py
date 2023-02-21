#List comprehensions and Codewars
list(map(str.upper,((''.join([chr(c+65).lower() for c in range(26)]+[chr(c+65).upper() for c in range(26)])))))
list(map(ord,((''.join([chr(c+65).lower() for c in range(26)]+[chr(c+65).upper() for c in range(26)])))))
list(map(str.lower,((''.join([chr(c+65).lower() for c in range(26)]+[chr(c+65).upper() for c in range(26)])))))
list(map(str.upper,((''.join([chr(c+65).lower() for c in range(26)]+[chr(c+65).upper() for c in range(26)])))))
list(map(bin,(map(ord,((''.join([chr(c+65).lower() for c in range(26)]+[chr(c+65).upper() for c in range(26)])))))))
#The problem description:Codewars: 
#https://www.linkedin.com/posts/emmanuel-pam-081b89ab_javascript-activity-7019302119526608896-z70M?utm_source=share&utm_medium=member_desktop
#Create a function that moves the first letter of each word to the end of it, 
#then add "ay" to the end of the word. Leave punctuation marks untouched.
#Examples:
#('Pig latin is cool'); // igPay atinlay siay oolcay
#('Hello world !'); // elloHay orldway !
[i[::-1]+str('ay') for i in 'Pig latin is cool'.split()]
igPay atinlay siay oolcay
[i[::-1]+str('ay') for i in 'Hello world !'.split() if i!='!']
elloHay orldway !