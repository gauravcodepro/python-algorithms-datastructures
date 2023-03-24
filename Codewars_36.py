https://www.linkedin.com/feed/update/urn:li:activity:7034847716920766464?utm_source=share&utm_medium=member_desktop
How to Check if a String is a Subsequence of another with Python?
a='abcde'
b='ace'
'True' if set(a).intersection(set(b))==set(b) else 'False'
#True
print(['True' if i in j else 'False' for i in list(a) for j in list(b)])
['True', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'True']