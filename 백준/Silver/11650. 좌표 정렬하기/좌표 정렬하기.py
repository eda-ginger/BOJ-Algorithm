n = int(input())

result = []
for _ in range(n):
    x, y = map(int, input().split())
    result.append((x, y))

for a, b, in sorted(result, key=lambda x:(x[0], x[1])):
    print(a, b)