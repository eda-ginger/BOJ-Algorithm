n = int(input())
sen = input()
HIARC = {'H':0, 'I':0, 'A':0, 'R':0, 'C':0}

for s in sen:
    if s in HIARC:
        HIARC[s] += 1

print(min(HIARC.values()))