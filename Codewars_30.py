str(input)=input(" enter a word: ")
'plays banjo' if str(input) in string.ascii_letters  else 'doesn't play banjo'
or 
str(input)=input(" enter a word: ")
'plays banjo' if str(input) in [[chr(c+65).upper() for c in range(26)]+[chr(c+65).lower() for c in range(26)]] else 'doesnt play banjo'
