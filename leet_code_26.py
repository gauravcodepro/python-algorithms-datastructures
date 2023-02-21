# Given any int find whether the given int is an arthimetic number or not. 
n=6
[print('True') if sum([i for i,id in enumerate(range(n),1) if n%i==0])
                            %len([i for i,id in enumerate(range(n),1) if n%i==0])==0 else "False"]
True
n=8
[print('True') if sum([i for i,id in enumerate(range(n),1) if n%i==0])
                            %len([i for i,id in enumerate(range(n),1) if n%i==0])==0 else "False"]
['False']