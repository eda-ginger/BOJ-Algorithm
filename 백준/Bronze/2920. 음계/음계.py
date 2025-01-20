scale = list(map(int, input().split()))
x = ''.join(map(str, scale))
asc = ''.join(map(str, sorted(scale, reverse=False)))
des = ''.join(map(str, sorted(scale, reverse=True)))
if x == asc:
    print('ascending')
elif x == des:
    print('descending')
else:
    print('mixed')