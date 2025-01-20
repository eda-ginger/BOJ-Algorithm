n = int(input())
for i in range(n):
    total = 0
    cont = 0
    sol = str(input())
    for s in sol:
        if s == 'O':
            cont = cont + 1
            total += cont
        else:
            cont = 0
    print(total)
        