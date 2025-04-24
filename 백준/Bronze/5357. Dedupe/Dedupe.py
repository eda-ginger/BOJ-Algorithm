n = int(input())
for _ in range(n):
    result = []
    current = ''
    lst = input()
    for idx, i in enumerate(lst):
        if current == '':
            current = i
            result.append(i)
        elif current == i:
            continue
        else:
            current = i
            result.append(i)
    print(''.join(result))