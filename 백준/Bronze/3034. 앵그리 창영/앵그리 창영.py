import math

n, w, l = map(int, input().split())
d = math.sqrt(w**2 + l**2)

for _ in range(n):
    f = int(input())
    
    if f <= d:
        print('DA')
    else:
        print('NE')
