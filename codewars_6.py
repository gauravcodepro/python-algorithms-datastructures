#https://www.codewars.com/kata/55143152820d22cdf00001bb
#5 kyu 
#count '9's from 1 to n
#It's 9 time!
#I want to count from 1 to n. How many times will I use a '9'?
#9, 19, 91.. will contribute one '9' each, 99, 199, 919.. wil contribute two '9's each...etc
#Note: n will always be a positive integer.
#Examples (input -> output)
#8  -> 0
#9  -> 1
#10 -> 1
#98 -> 18
#100 -> 20
"""
simple map the iterator and count, called two map and one iterator. 
"""
sum(list(map(lambda n: n.count('9'),[list(i) for i in list(map(str,([i for i in range (1,100,1)])))])))