n = int(input())
for _ in range(n):
    result = []
    lst = input()
    current = ''
    for i in lst:
        if i != current:
            result.append(i)
            current = i
    print(''.join(result))