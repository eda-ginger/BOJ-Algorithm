# 점수/M*100 (m은 최댓값)
n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
nlst = [l/m*100 for l in lst]
print(sum(nlst) / len(nlst))