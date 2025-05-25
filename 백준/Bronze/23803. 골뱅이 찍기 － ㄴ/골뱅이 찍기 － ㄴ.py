n = int(input())
num = n * 5

for idx in range(num):
    if idx >= n * 4:
        print('@' * num)
    else:
        print('@' * n)
