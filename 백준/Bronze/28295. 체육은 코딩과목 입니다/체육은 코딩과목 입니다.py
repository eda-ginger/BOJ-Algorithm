init = 0
dn = {1: 90, 2: 180, 3:-90}
p = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
for i in range(10):
    n = int(input())
    init += dn[n]
rn = init % 360
print(p[rn])