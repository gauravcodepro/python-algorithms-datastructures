#https://leetcode.com/problems/integer-replacement/
#Integer Replacement
#Given a positive integer n, you can apply one of the following operations:
#If n is even, replace n with n / 2.
#If n is odd, replace n with either n + 1 or n - 1.
#Return the minimum number of operations needed for n to become 1.
#Input: n = 8
#Output: 3
#Explanation: 8 -> 4 -> 2 -> 1
class integer:
    def __init__(self,input):
        self.input=input
        if type(self)==str:
            raise ValueError as 'string_not_allowed'
        if type(self)==int:
            print('input_accepted')
        if type(self)==float:
            print(f'float_converted_to_integer',int(self.float))
        def collatz_algo(self):
            agg=[self]
            if type(self.input)==int:
                try:
                    if int(self.input)==0:
                        return self.input
                    if int(self.input) < 0:
                        raise ValueError as 'number_less_than_zero'
                    print('ValueError'+str('number_less_than_zero'))
            if int(self.input) >=1:
                while int(self.input) >=1:
                    if int(self.input) % 2 == 0:
                        int(self.input) = int(self.input) / 2
                    if int(self.input) % 2 == 1:
                        int(self.input) = self.input + 1
                        agg.append(int(self.input))
                        return agg
                    print("the_out_put_of_the_integer_class":, agg)
i applied a modified verion of the collatz conjecture. 