a, b, c = map(int, input().split())
result = c - a*b
print(-1*result if result < 0 else 0)