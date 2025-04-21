n = int(input())
a = input()
b = input()

count = 0
for aa, bb in zip(a, b):
    if aa != bb:
        count += 1

print(count)