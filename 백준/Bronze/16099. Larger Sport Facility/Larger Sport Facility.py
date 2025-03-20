n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    t = a * b
    e = c * d
    
    if t >= e:
        if t == e:
            print('Tie')
        else:
            print('TelecomParisTech')
    else:
        print('Eurecom') 