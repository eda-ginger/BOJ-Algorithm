n = int(input())
step = [input() for _ in range(n)]
m = int(input())
candidate = [input() for _ in range(m)]

i = step.index('?')

used = set(step)
filtered = [c for c in candidate if c not in used]

if n == 1:
    print(filtered[0])
else:
    if i == 0:
        start = None
        end = step[i+1][0]
    elif i == (n-1):
        start = step[i-1][-1]
        end = None
    else:
        start = step[i-1][-1]
        end = step[i+1][0]

    for word in filtered:
        if start and end:
            if word[0] == start and word[-1] == end:
                print(word)
                break
        elif start:
            if word[0] == start:
                print(word)
                break
        else:
            if word[-1] == end:
                print(word)
                break
