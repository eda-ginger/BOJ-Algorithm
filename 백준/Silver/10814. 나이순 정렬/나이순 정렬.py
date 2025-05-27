n = int(input())
box = {}
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age in box.keys():
        box[age] += [name]
    else:
        box[age] = [name]

box = dict(sorted(box.items()))
for k, v in box.items():
    for vv in v:
        print(k, vv)