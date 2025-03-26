# (a2+b2+m)/(ab)
def find(n, m):
    count = 0
    for a in range(1, n):
        for b in range(a+1, n):
            cal = (a**2 + b**2 + m) / (a*b)
            if int(cal) == cal:
                count += 1
    return count

num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    print(find(n, m))