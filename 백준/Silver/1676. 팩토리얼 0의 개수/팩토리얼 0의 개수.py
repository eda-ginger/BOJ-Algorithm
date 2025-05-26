n = int(input())

np = 1
for i in range(n, 0, -1):
    np *= i   

count = 0
for s in str(np)[::-1]:
    if s != '0':
        break
    else:
        count += 1

print(count)