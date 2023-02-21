s='abcd'
t='abcde'
([t for t in list(t) if t not in list(s)],[s for s in list(s) if s in list(t)])
#(['e'], ['a', 'b', 'c', 'd'])
a="1234"
[i for i in list(map(bin,map(int,list(a)))) if '1' and '0' in i]
#['0b1', '0b10', '0b11', '0b100']