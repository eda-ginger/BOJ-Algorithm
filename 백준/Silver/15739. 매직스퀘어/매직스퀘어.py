def is_magic(matrix):
    n = len(matrix)
    target = sum(matrix[0])  # 기준 합

    # 중복 확인
    flat = [num for row in matrix for num in row]
    if len(flat) != len(set(flat)):
        return False

    # 행의 합 확인
    for row in matrix:
        if sum(row) != target:
            return False

    # 열의 합 확인
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != target:
            return False

    # 주대각선 확인
    if sum(matrix[i][i] for i in range(n)) != target:
        return False

    # 반대대각선 확인
    if sum(matrix[i][n - 1 - i] for i in range(n)) != target:
        return False

    return True

# 입력
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 출력
print("TRUE" if is_magic(matrix) else "FALSE")
