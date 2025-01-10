a = int(input())
b = list(map(int, input().split()))
min_b = min(b)
max_b = max(b)

if a == 1:
    print(b[0] ** 2)
else:
    print(min_b * max_b)