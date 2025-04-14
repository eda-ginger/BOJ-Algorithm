def cl(lst):
    return max(lst) - min(lst)

n = int(input())
xs, ys = [], []
for idx in range(n):
    a, b, c, d = map(int, input().split())
    xs.extend([a, c])
    ys.extend([b, d])
    print((2 * cl(xs)) + (2 * cl(ys)))
