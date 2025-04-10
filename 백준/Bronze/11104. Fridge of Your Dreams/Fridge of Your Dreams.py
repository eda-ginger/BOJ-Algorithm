n = int(input())
for _ in range(n):
    bit24 = [2**(e) * int(i) for e, i in enumerate(input()[::-1])]
    print(sum(bit24))