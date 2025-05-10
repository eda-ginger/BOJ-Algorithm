n = int(input())
lst = list(map(int, input().split()))
t, p = map(int, input().split())

to = 0
for l in lst:
    if l % t == 0:
        to += l // t
    else:
        to += (l // t) + 1

po = (n // p), (n % p)

print(to)
print(po[0], po[1])