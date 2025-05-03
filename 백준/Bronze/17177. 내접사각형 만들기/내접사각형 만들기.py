import math

def solve(a, b, c):
    p = a
    q = 2 * b * c
    r = a * (c * c - a * a + b * b)

    d = q * q - 4 * p * r
    if d < 0:
        return -1

    x = (-q + math.sqrt(d)) / (2 * p)
    if x < 0:
        return -1

    return int(x + 1e-5)

# 입력 처리
a, b, c = map(int, input().split())
print(solve(a, b, c))
