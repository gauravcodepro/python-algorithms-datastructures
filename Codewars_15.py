#https://www.codewars.com/kata/5782dd86202c0e43410001f6
#Your task is to write a function named do_math that receives a single argument. 
# This argument is a string that contains multiple whitespace delimited numbers. 
# Each number has a single alphabet letter somewhere within it.
#Example : "24z6 1x23 y369 89a 900b"
#As shown above, this alphabet letter can appear anywhere within the number. You have to extract the letters and 
# sort the numbers according to their corresponding letters.
#Example : "24z6 1x23 y369 89a 900b" will become 89 900 123 369 246 (ordered according to the alphabet letter)
#Here comes the difficult part, now you have to do a series of computations on the numbers you have extracted.
#The sequence of computations are + - * /. Basic math rules do NOT apply, you have to do each computation in exactly this order.
#This has to work for any size of numbers sent in (after division, go back to addition, etc).
#In the case of duplicate alphabet letters, you have to arrange them according to the number that appeared first in the input string.
#Remember to also round the final answer to the nearest integer.
#Examples :
#"24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299
#"24z6 1z23 y369 89z 900b" = 900 + 369 - 246 * 123 / 89 = 1414
#"10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60

a="24z6 1x23 y369 89a 900b"
# sorting according to the alphabet in the reverse order
sorted([sorted(i) for i in ([list(i) for i in list(a.split())])],key=lambda n:n[-1])
[['8', '9', 'a'],
 ['0', '0', '9', 'b'],
 ['1', '2', '3', 'x'],
 ['3', '6', '9', 'y'],
 ['2', '4', '6', 'z']]
# sorting according to the alphabet in the sorted order
[sorted([[i for i in j if i.isalpha()]+[i for i in j if i.isdigit()] for j in ([i for i in list(a.split())])],key=lambda n: n[0])]
[[['a', '8', '9'],
  ['b', '9', '0', '0'],
  ['x', '1', '2', '3'],
  ['y', '3', '6', '9'],
  ['z', '2', '4', '6']]]
# extracting all the digits from the string
[''.join([i for i in j if i.isdigit()]) for j in sorted([[i for i in j if i.isalpha()]+
                                    [i for i in j if i.isdigit()] for j in ([i for i in list(a.split())])],key=lambda n: n[0])]
['89', '900', '123', '369', '246']

#extracting all the digits from the string in the form of the ints
list(map(int,[''.join([i for i in j if i.isdigit()]) for j in sorted([[i for i in j if i.isalpha()]+[i for i in j 
                                    if i.isdigit()] for j in ([i for i in list(a.split())])],key=lambda n: n[0])]))
[89, 900, 123, 369, 246]
# indexed lists of lists for any calculations according to the list[0]
sorted([([i for i in i if i.isalpha()]+[int(''.join([i for i in i if i.isdigit()]))]) for i in list(a.split())],key=lambda n:n[0])
[['a', 89], ['b', 900], ['x', 123], ['y', 369], ['z', 246]]
# Any type of calculations given a combination of string and ints
a="24z6 1x23 y369 89a 900b"
"24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299
([i for i in sorted([([i for i in i if i.isalpha()]+[int(''.join(
    [i for i in i if i.isdigit()]))]) for i in list(a.split())],key=lambda n:n[0])]
       [0][1]+[i for i in sorted([([i for i in i if i.isalpha()]+[int(''.join([i for i in i if i.isdigit()]))]) 
          for i in list(a.split())],key=lambda n:n[0])][1][1]-[i for i in sorted([([i for i in i if i.isalpha()]
             +[int(''.join([i for i in i if i.isdigit()]))]) 
                    for i in list(a.split())],key=lambda n:n[0])][2][1])*
[i for i in sorted([([i for i in i if i.isalpha()]+[int(''.join([i for i in i if i.isdigit()]))]) 
                     for i in list(a.split())],key=lambda n:n[0])][3][1]/[i for i in sorted([([i for i in i if i.isalpha()]+
                    [int(''.join([i for i in i if i.isdigit()]))]) for i in list(a.split())],key=lambda n:n[0])][4][1]