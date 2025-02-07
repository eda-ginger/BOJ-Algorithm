d = {"fdsajkl;": 'in-out', "jkl;fdsa": 'in-out', 
     "asdf;lkj": 'out-in', ";lkjasdf": 'out-in',
     "asdfjkl;": 'stairs', ";lkjfdsa": 'reverse'}
s = input()
if s in d:
    print(d[s])
else:
    print('molu')