lst = [i for i in input()]
s = set(lst)
result = []
for sn in s:
    if lst.count(sn) % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

if ('even' in result) and ('odd' in result):
    print('0/1')
else:
    if 'even' in result:
        print('0')
    else:
        print('1')