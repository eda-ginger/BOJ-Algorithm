def win(name):
    l, o, v, e = name.count('L'), name.count('O'), name.count('V'), name.count('E')
    return ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100

your_name = input()
num_teams = int(input())

best_score = -1
best_team = ""

for _ in range(num_teams):
    team = input()
    combined = your_name + team
    score = win(combined)

    if score > best_score or (score == best_score and team < best_team):
        best_score = score
        best_team = team

print(best_team)
