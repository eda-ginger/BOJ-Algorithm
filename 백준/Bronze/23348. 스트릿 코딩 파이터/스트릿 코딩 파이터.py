a, b, c = map(int, input().split())
n = int(input())
score = 0
for t in range(n):
    t_score = 0
    for i in range(3):
        ai, bi, ci = map(int, input().split())
        t_score += a*ai + b*bi + c*ci
    score = max(t_score, score)
print(score)