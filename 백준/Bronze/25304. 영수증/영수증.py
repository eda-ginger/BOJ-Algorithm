total = int(input())
items = int(input())

cal = 0
for i in range(items):
    price, count = map(int, input().split())
    cal += price * count

if cal == total:
    print('Yes')
else:
    print('No')
        