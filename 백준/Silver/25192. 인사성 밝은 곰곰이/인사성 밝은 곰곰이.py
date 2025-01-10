times = int(input())

bear = 0
nicknames = {}
for t in range(times):
    line = str(input())
    if line == 'ENTER':
        nicknames = {}
    else:
        if line in nicknames:
            continue
        else:
            nicknames[line] = 1
            bear += 1
print(bear)          
    