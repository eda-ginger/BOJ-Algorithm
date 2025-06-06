n = int(input())
pie = 3.14159
vols = []
for _ in range(n):
    lst = input().split()
    if lst[0] == 'S':
        vols.append((4/3)*pie*float(lst[1])**3)
    elif lst[0] == 'L':
        vols.append(pie*float(lst[1])**2*float(lst[2]))
    else:
        vols.append((1/3)*pie*float(lst[1])**2*float(lst[2]))
print(max(vols))
        