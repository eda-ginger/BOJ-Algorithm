a, b, c = map(int, input().split())

d = {k:[a, b, c].count(k) for k in [a, b, c]}
d = sorted(d.items(), key=lambda x: x[1], reverse=True)

if d[0][1] == 3:
    print(10000 + d[0][0] * 1000)
elif d[0][1] == 2:
    print(1000 + d[0][0] * 100)
else:
    print(max(a, b, c) * 100)
