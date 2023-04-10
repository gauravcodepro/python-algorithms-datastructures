#https://leetcode.com/problems/find-median-from-data-stream/
#Find Median from Data Stream
#The median is the middle value in an ordered integer list. 
#If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#For example, for arr = [2,3,4], the median is 3.
#For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
#Implement the MedianFinder class:
#MedianFinder() initializes the MedianFinder object.
#void addNum(int num) adds the integer num from the data stream to the data structure.
#double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
class median_nested_even:
    def __init__(self,arr:list) -> list:
        self.arr=arr
        if len(self.arr)==0:
            return []
        print(f'the_array_is_null:'{}.format(len(self.arr)))
    '''
    median of the nested list of lists if the nested list are even
    '''
    def median(self):
        for i in self.input:
                if type(i)==list:
                    print('type_accepted')
                    if type(i) != list:
                        raise TypeError
                    print(f'TypeError'+str('type_not_accepted'))
                    if len(self.input)%2==1:
                        print(f'the_array_is_odd:'{}.format(len(self.input)%2))
                        median_value=[]
                        if len(self.input)%2==0:
                            n=[len(i)//2 for i in self.input]
                            median_value.append([sum(i)/2 for i in ([(i[0][-1],i[1][0])
                                                    for i in ([([sorted(self.input[i])
                                                for i in range(len(self.input))][i][:n[i]],[sorted(self.input[i])
                                                                      for i in range(len(self.input))][i][n[i]:])
                                                                for i in (sorted(range(len([sorted(self.input[i])
                                                                       for i in range(len(self.input))]))))])])])
                            return median_value
                        print(f'The_median_of_given_array:'{}.format(median_value))
class median_nested_odd:
    def __init__(self,arr:list) -> list:
        self.arr=arr
        if len(self.arr)==0:
            return []
        print(f'the_array_is_null:'{}.format(len(self.arr)))
    '''
    median of the nested list of the lists are odd
    '''
    def median(self):
        for i in self.input:
                if type(i)==list:
                    print('type_accepted')
                    if type(i) != list:
                        raise TypeError
                    print(f'TypeError'+str('type_not_accepted'))
                    if len(self.input)%2==1:
                        print(f'the_array_is_odd:'{}.format(len(self.input)%2))
                        median_value=[]
                        if len(self.input)%2==0:
                            median_value=[]
                            median_value.append(list(set([[sorted(self.input[i]) for i in range(len((self.input)))][i][j-1]
                                             for i in range(len([sorted(self.input[i]) for i in range(len((self.input)))]))
                                                                    for j in [(len(i)+1)//2 for i in [sorted(self.input[i])
                                                                                    for i in range(len((self.input)))]]])))
                            return median_value
                        print(f'the_median_value_of_the_array:'.format(median_value))
class median_even(list_utils): #median of the list if it is even
    super().__init__()
    def median(self):
        for i in self.input:
                if type(i)==list:
                    print('type_accepted')
                    if type(i) != list:
                        raise TypeError as type_not_accepted
                    print(f'TypeError'+str(type_not_accepted))
                    if len(self.input)%2==1:
                        print(f'the_array_is_odd:'{}.format(len(self.input)%2))
                        median_value=[]
                        if len(self.input)%2==0:
                            n=len(self.input)//2
                            median_value.append([sum(i)/2 for i in ((i[0][-1],i[1][0]) 
                              for i in ((i[:n],i[n:]) for i in [sorted(self.input)]))])
                            return median_value
                        print(f'The_median_of_given_array:'{}.format(median_value))
class median_odd(list_utils): #median of the list if it is odd
    super().__init__()
    def median(self):
        for i in self.input:
                if type(i)==list:
                    print('type_accepted')
                    if type(i) != list:
                        raise TypeError as type_not_accepted
                    print(f'TypeError'+str(type_not_accepted))
                    if len(self.input)%2==0:
                        print(f'the_array_is_even:'{}.format(len(self.input)%2))
                        median_value=[]
                        if len(self.input)%2==0:
                            median_value.append([(i) for i,id in enumerate(sorted(self.input),1) 
                            if (int((len(sorted(self.input))+1)//2))==i])
                            return median_value
                        print(f'The_median_of_given_array:'{}.format(median_value))