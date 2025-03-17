n = int(input())

print('int a;')
for i in range(n):
    c = i + 1
    if c == 1:
        print('int *ptr = &a;')
    elif c == 2:
        print('int **ptr2 = &ptr;')
    else:
        print(f"int {'*'*c}ptr{c} = &ptr{c-1};")
