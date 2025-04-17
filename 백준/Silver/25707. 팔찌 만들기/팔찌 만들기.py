def bracelet(lst):
    chi = 0
    slst = sorted(lst)
    for i in range(len(slst)):
        if i == len(slst) - 1:
            chi += slst[i] - slst[0]
        else:
            chi += slst[i+1] - slst[i]
    return chi

n = int(input())
lst = list(map(int, input().split()))
print(bracelet(lst))