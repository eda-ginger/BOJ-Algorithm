idx = [i for i in range(1, 31)]
for i in range(28):
    a = int(input())
    idx.remove(a)
print(min(idx))
print(max(idx))