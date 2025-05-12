import itertools

n, m = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
for i in itertools.combinations(lst, 3):
    total = sum(i)
    if total <= m and total > result:
        result = total
print(result)
