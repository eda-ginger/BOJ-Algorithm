# C = number of points (exist same coordinates)
# N = size of paper
N, C = map(int, input().split())
origin = N * N
remain = (N, N)
for _ in range(C):
    x, y = map(int, input().split())
    
    if x > remain[0] or y > remain[1]:
        continue
    
    # size
    horizon = x * remain[1]
    vertical = y * remain[0]
    
    if horizon >= vertical:
        remain = (x, remain[1])
    else:
        remain = (remain[0], y)

print(remain[0] * remain[1])
