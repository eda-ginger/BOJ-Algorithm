# B와 W의 차이값이 최소가 되게
# 8X8 사이즈 filter를 제작하여 이동시키기

def min_repaint(b, r, c):
    colors = ['B', 'W']
    result = float('inf')

    for first in colors:
        count = 0
        for i in range(8):
            for j in range(8):
                expected = first if (i+j) % 2 == 0 else ('B' if first == 'W' else 'W')
                if b[r+i][c+j] != expected:
                    count += 1
        result = min(result, count)
    return result

m, n = map(int, input().split())
board = [input() for _ in range(m)]

min_result = float('inf')
for mm in range(m-7):
    for nn in range(n-7):
        min_result = min(min_result, min_repaint(board, mm, nn))
print(min_result)