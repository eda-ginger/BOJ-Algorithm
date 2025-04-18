from math import trunc

def dfs(money, year):
    global answer
    answer = max(answer, money)
    if year >= 1:
        dfs(trunc(money * 1.05), year - 1)
    if year >= 3:
        dfs(trunc(money * 1.2), year - 3)
    if year >= 5:
        dfs(trunc(money * 1.35), year - 5)

money, year = map(int, input().split())
answer = 0
dfs(money, year)
print(answer)
