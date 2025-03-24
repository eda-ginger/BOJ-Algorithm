n = int(input())
sl = sorted(list(map(int, input().split())), reverse=True)
print(sl[0] - sl[-1])