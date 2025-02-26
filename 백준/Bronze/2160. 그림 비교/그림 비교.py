import sys
n = int(input())
lsts = [[sys.stdin.readline().strip() for _ in range(5)] for _ in range(n)]


def compare(a, b):
    diff = 0
    for x1, x2 in zip(a, b):
        for r1, r2 in zip(x1, x2):
            if r1 != r2:
                diff += 1
    return diff

result = (0, 0)
min_diff = float('inf')  

for idx1 in range(n):
    for idx2 in range(idx1 + 1, n):
        diff = compare(lsts[idx1], lsts[idx2])
        if diff < min_diff:
            min_diff = diff
            result = (idx1 + 1, idx2 + 1) 

print(*result)
