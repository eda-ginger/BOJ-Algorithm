def strawberry(num):
    bn = bin(num)[2:].zfill(4)
    st = bn.replace('0', 'V').replace('1', '딸기')
    return st

lst = list(range(1, 16)) + list(range(14, 1, -1))

n = int(input())
for _ in range(n):
    sp = int(input())
    step = lst[(sp - 1) % len(lst)]
    print(strawberry(step))