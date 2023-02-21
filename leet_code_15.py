#Integer to English Words (Hard)
#Convert a non-negative integer num to its English words representation.
# Example 1:
#Input: num = 123
#Output: "One Hundred Twenty Three"
#Example 2:
#Input: num = 12345
#Output: "Twelve Thousand Three Hundred Forty Five"
#Example 3:
#Input: num = 1234567
#Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# using simple map: map the ord values and then map the chr values and construct the statement
[''.join(list(map(lambda n: chr(n),(list(map(lambda n: ord(n),i)))))) for i in (i.lower()for i in ((i for i in a.split())))]
['one', 'hundred', 'twenty', 'three']
#using combinations list all the combinations and then fetch the tuple
print([i for i in list(combinations((map(lambda n: ord(n),[i.lower() for i in {chr(c+65) for c in range(26)}])),3))])
#making the dictionary combinations and printing out the combination in snake case or camel case
([i for i in ([list(map(lambda n: ord(n),[i.lower() for i in {chr(c+65) for c in range(26)}]))])],
                            [[i for i in ([list(map(lambda n: ord(n),[i for i in {chr(c+65) for c in range(26)}]))])]])