n = int(input())
s = n % 8
if s == 1:
    print(1)
elif s in [2, 0]:
    print(2)
elif s in [3, 7]:
    print(3)
elif s in [4, 6]:
    print(4)
else:
    print(5)
    