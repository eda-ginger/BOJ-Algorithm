total = []
for i in range(5):
    s = int(input())
    if s > 40:
        total.append(s)
    else:
        total.append(40)
print(round(sum(total) / 5))