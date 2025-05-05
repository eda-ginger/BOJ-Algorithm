n, h = map(int, input().split())
l = list(map(int, input().split()))

i = 0
while True:
    if h <= l[i % n]:
        h += 1
        i += 1
    else:
        print((i % n) + 1)
        break