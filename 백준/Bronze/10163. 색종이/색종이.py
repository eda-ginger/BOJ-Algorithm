n = int(input())
paper = []  # 색종이 좌표 리스트

for _ in range(n):
    x, y, w, h = map(int, input().split())
    coords = []
    for i in range(x, x + w):
        for j in range(y, y + h):
            coords.append((i, j))
    paper.append(coords)

seen = set()
visible_area = [0] * n  # 색종이 보이는 면적 리스트

# 마지막 색종이부터 순회 (뒤에서부터 붙은 색종이 우선)
for idx in reversed(range(n)):
    for coord in paper[idx]:
        if coord not in seen:
            seen.add(coord)
            visible_area[idx] += 1

# 출력
for count in visible_area:
    print(count)