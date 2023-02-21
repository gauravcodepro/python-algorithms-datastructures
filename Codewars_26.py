#All that you can do on parenthesis
#creating parentheses
print([i for i in (list(map(lambda n: ''.join(n),list(permutations(s))))) if i.startswith('(') and i.endswith(')')])
['(())', '(())', '()()', '()()', '(())', '(())', '()()', '()()']
print(set([i for i in (list(map(lambda n: ''.join(n),list(permutations(s))))) if i.startswith('(') and i.endswith(')')]))
#function for calculating balanced parentheses
s='()()()()))))(((((('
def parentheses(s):
front=[]
back=[]
for i in list(s):
    if i==('('):
        front.append(i.count('('))
    if i==(')'):
        back.append(i.count(')'))
    if (sum(front)+sum(back))%2==0:
        print('True')
#one line approach for calculating balanced parentheses for .apply() and np.where 
# across the dataframes in case of the codes
print((s.count('(')+s.count(')'))%2==0)
# across numpy
np.where((s.count('(')+s.count(')'))%2==0)
np['col'] = np['col'].str.contains=whatever condition true or false