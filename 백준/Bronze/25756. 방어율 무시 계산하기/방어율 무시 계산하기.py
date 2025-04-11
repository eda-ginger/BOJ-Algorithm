def cal_defence_ratio(v, a):
    return 1 - (1 - v)*(1 - a)

v = 0
n = int(input())
l = list(map(int, input().split()))
for a in l:
    v = cal_defence_ratio(v, a*0.01)
    print(f"{v*100:.06f}")