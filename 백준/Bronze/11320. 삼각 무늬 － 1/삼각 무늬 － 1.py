t = int(input())
for i in range(t):
    a, b = map(int, input().split()) # b <= a, a/b available
    sa = a**2
    sb = b**2
    if sa % sb > 0:
        print((sa//sb) + 1)
    else:
        print(sa//sb)