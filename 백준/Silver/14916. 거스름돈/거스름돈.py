n = int(input())

result = 100000

n5 = n // 5
for i in range(0, n5+1):
    ni = n - (5*i)
    if ni == 0:
        coins = i
        if coins < result:
            result = coins

    if ni % 2 == 0:
        n2 = ni // 2
        coins = i + n2
        if coins < result:
            result = coins

if result != 100000:
    print(result)
else:
    print(-1)
