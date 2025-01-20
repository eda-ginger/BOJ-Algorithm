s = set()
for i in range(10):
    num = int(input()) % 42
    s.add(num)
print(len(s))