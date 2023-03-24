#https://www.linkedin.com/posts/codewars_multi-line-task-hello-world-activity-7043159451868000256-h9na?utm_source=share&utm_medium=member_desktop
#https://www.codewars.com/kata/5935558a32fb828aad001213
#You need to write a function f that returns the string Hello, world!.
#Requirement: Every line must have at most 2 characters, 
#and total number of lines must be less than 40.
#Hint: It's possible to complete this in 28 lines only.
for i in range(len(list(filter(lambda n: n in [chr(c+65) for c in range(26)]+[chr((c+65)-32) for c in range(26)]+[chr((c+65)+32) for c in range(26)],
                [row for col in list(map(lambda n: list(n),re.split(r'"\n"',s))) for row in col])))-1):
    print(list(filter(lambda n: n in [chr(c+65) for c in range(26)]+[chr((c+65)-32) for c in range(26)]+[chr((c+65)+32) for c in range(26)],
                [row for col in list(map(lambda n: list(n),re.split(r'"\n"',s))) for row in col]))[i],list(filter(lambda n: n in [chr(c+65) for c in range(26)]+[chr((c+65)-32) for c in range(26)]+[chr((c+65)+32) for c in range(26)],
                [row for col in list(map(lambda n: list(n),re.split(r'"\n"',s))) for row in col]))[i+1])
H e
e l
l l
l o
o ,
, w
w o
o r
r l
l d
d !

if you want to add a return statement then you can add '/n'.join(for i in range(len(list(filter(lambda n: n in [chr(c+65) for c in range(26)]+[chr((c+65)-32) for c in range(26)]+[chr((c+65)+32) for c in range(26)],
                [row for col in list(map(lambda n: list(n),re.split(r'"\n"',s))) for row in col])))-1):
    print(list(filter(lambda n: n in [chr(c+65) for c in range(26)]+[chr((c+65)-32) for c in range(26)]+[chr((c+65)+32) for c in range(26)],
                [row for col in list(map(lambda n: list(n),re.split(r'"\n"',s))) for row in col]))[i],list(filter(lambda n: n in [chr(c+65) for c in range(26)]+[chr((c+65)-32) for c in range(26)]+[chr((c+65)+32) for c in range(26)],
                [row for col in list(map(lambda n: list(n),re.split(r'"\n"',s))) for row in col]))[i+1]))