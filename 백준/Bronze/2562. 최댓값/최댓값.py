l = []
for i in range(9):
    l.append((i+1, int(input())))
ml = max(l, key=lambda x: x[1])
print(ml[1])
print(ml[0])