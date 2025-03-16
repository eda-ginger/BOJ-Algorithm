a, b, c = input().split()
if b == 'AND':
    if a == 'true' and c == 'true':
        print('true')
    else:
        print('false')
else:
    if a == 'false' and c == 'false':
        print('false')
    else:
        print('true')
    