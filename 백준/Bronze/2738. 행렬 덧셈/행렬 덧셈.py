import sys

n, m = map(int, sys.stdin.readline().split())
first = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
second = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    result = [first[i][j] + second[i][j] for j in range(m)]
    print(' '.join(map(str, result)))