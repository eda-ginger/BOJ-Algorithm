n = int(input())

result = []
for _ in range(n):
    s = input()
    if s not in result:
        result.append(s)

for i in sorted(result, key=lambda x: (len(x), x)):
    print(i)
