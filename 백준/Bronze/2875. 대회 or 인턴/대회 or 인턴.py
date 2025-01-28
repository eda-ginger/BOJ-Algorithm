w, m, k = map(int, input().split())

team = 0
for i in range(k):
    if w // 2 >= m:
        w -= 1
    else:
        m -= 1

print(min(w//2, m))