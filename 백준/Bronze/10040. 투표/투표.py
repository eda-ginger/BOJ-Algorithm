n, m = map(int, input().split())
lst1 = [int(input()) for _ in range(n)]
lst2 = [int(input()) for _ in range(m)]
result = {}
for l2 in lst2:
    select = [(idx, l1) for idx, l1 in enumerate(lst1) if l1 <= l2]
    result[select[0][0]] = result.get(select[0][0], 0) + 1
print(max(result, key=result.get) + 1)