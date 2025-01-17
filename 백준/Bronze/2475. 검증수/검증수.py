l = list(map(int, input().split()))
l2 = [i**2 for i in l] 
print(sum(l2)%10)