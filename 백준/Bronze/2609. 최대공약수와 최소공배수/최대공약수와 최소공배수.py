def find_common(a, b):
    m = min(a, b)
    common = 1
    for i in range(2, m+1):
        if a % i == 0 and b % i == 0:
            common = i
    multiple = a*b // common
    return common, multiple

a, b = map(int, input().split())
c, m = find_common(a, b)
print(c)
print(m)