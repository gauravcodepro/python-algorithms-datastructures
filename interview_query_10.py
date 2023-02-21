#https://www.interviewquery.com/questions/data-stream-median
#Data Stream Median
#Question
#Write a function data_stream_median to calculate the new median from a stream of ordered integers and the 
# new element which is not yet inserted into the stream.
#The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, 
# so the median is the mean of the two middle values.
#Example:
#new_value = 2
#stream = [1, 2, 3, 4, 5, 6]
#def data_stream_median(new_value, stream): -> 3

Median of stream before inserting the value:
stream = [1, 2, 3, 4, 5, 6]
[sum(i)/2 for i in ((i[0][-1],i[1][0])
            for i in ((i[:3],i[3:]) for i in [sorted(stream)]))]
[3.5]

Median of stream after inserting the value:
stream = [1, 2, 2, 3, 4, 5, 6]
[print(i,id) for i,id in enumerate(sorted(stream),1)
                        if (int((len(sorted(stream))+1)//2))==i]
[4 3]