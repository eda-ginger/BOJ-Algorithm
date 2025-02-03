n = map(int, input())
l = list(map(int, input().split()))
c = 0

def prime(num):
    if num <= 1:
        return False
    for ii in range(2, num):
        if num % ii == 0:
            return False
    return True

for i in l:
    if prime(i):
        c +=1
        
print(c)
    