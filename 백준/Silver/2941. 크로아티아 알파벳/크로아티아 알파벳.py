cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = str(input())

cnt = 0
for i in cro:
    cnt += word.count(i)
    word = word.replace(i, '0')

word = word.replace('0', '')
print(cnt + len(word))

