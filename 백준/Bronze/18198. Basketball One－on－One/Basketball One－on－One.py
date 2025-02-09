scores = input()
re = [(scores[i], scores[i+1])  for i in range(0, len(scores), 2)]
s = {'A': 0, 'B': 0}
for r in re:
    who, plus = r
    s[who] += int(plus)
    if s['A'] >= 11 or s['B'] >= 11:
        if abs(s['A'] - s['B']) >= 2:
            print(max(s, key=s.get))
            break
        
