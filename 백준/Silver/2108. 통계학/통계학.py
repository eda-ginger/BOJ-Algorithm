import sys
N = int(input())

data = []
count = {}
for i in range(N):
    new = int(sys.stdin.readline().strip())
    data.append(new)
    if new in count:
        count[new] += 1
    else:
        count[new] = 1


print(round(sum(data) / N))
print(sorted(data)[N//2]) 

modes = [k for k in count.keys() if count[k] == max(count.values())]
if len(modes) > 1:
    print(sorted(modes)[1])
else:
    print(modes[0])
print(max(data) - min(data))

