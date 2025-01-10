N = int(input())

meets = {}
appear_chong = False
for i in range(N):
    meet = list(map(str, input().split()))
    if 'ChongChong' in meet:
        appear_chong = True
        meets[meet[0]] = meet[1]
        meets[meet[1]] = meet[0]
    else:
        if appear_chong:
            if meet[0] in meets or meet[1] in meets:
                meets[meet[0]] = meet[1]
                meets[meet[1]] = meet[0]
print(len(meets))
