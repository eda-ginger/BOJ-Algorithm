h, m = map(int, input().split())
t = int(input())

plus_hour = t // 60
plus_min = t % 60

ph = h + plus_hour
pm = m + plus_min

if pm >= 60:
    ph += 1
    pm = pm - 60

ph = ph % 24    
print(ph, pm)