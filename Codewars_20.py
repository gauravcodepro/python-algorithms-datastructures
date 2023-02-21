#Codewars hashtag generator
s= 'hello world'
print([str('#')+str().join([i.title() for i in s.split()])]) if 
                            len([str('#')+str().join([i.title() for i in s.split()])]) > 10 else print('Falsetry again'))