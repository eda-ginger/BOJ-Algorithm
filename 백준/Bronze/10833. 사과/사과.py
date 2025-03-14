n = int(input())
total = 0
for _ in range(n):
    a, b = map(int, input().split())
    total += b % a
print(total)