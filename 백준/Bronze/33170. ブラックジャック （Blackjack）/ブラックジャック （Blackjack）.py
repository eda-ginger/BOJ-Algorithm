a, b, c = open(0)
n = sum(list(map(int, [a, b, c])))
print(1 if n <= 21 else 0)