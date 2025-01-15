v_team = list(map(int, input().split()))
h_team = list(map(int, input().split()))

print(v_team[0]*6 + v_team[1]*3 + v_team[2]*2 + v_team[3]*1 + v_team[4]*2, end=' ')
print(h_team[0]*6 + h_team[1]*3 + h_team[2]*2 + h_team[3]*1 + h_team[4]*2)