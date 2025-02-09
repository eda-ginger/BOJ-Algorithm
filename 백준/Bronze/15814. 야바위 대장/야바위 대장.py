s = {idx: s for idx, s in enumerate(input())}
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    aa, bb = s[a], s[b]
    s[a] = bb
    s[b] = aa 
print(''.join(s.values()))