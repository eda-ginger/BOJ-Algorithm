n = int(input())
count = 0
for _ in range(n):
    s = str(input())
    if ('01' in s) or ('OI' in s):
        count += 1
print(count)