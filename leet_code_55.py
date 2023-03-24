https: // leetcode.com/problems/count-and -say/
The count-and -say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings
such that each substring contains exactly one unique digit. Then for each substring,
say the number of digits, then say the digit. Finally, concatenate every said digit.
For example, the saying and conversion for digit string "3322251":
a = "3322251"
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
a = "3322251"
b = [(i, list(map(lambda n: int(n), list(a))).count(i))
     for i in sorted(set(list(map(lambda n: int(n), list(a)))))]
''.join((map(str, [j for i in [j for i in ([list(map(lambda n: n[::-1], b))]) for j in i][1:] +
                   [j for i in ([list(map(lambda n: n[::-1], b))]) for j in i][:1] for j in i])))
'32231511'
