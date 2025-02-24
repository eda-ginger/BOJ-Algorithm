n = int(input())
a, b, c = map(int, input().split())
print(sum([min(n, i) for i in [a, b, c]]))