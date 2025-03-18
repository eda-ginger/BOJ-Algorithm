N = int(input())  # 이진수의 길이
M = input()       # 이진수 문자열
K = int(input())  # 2^K로 나누어 떨어지는지 확인

# K가 0이면 모든 수는 2^0 = 1로 나누어 떨어짐
if K == 0:
    print("YES")
# K가 N보다 크면, 마지막 K개의 비트를 확인할 수 없으므로
# 문자열에 1이 있는지 확인
elif K > N:
    if '1' in M:
        print("NO")
    else:
        print("YES")
else:
    # 마지막 K개의 비트가 모두 0인지 확인
    if '1' in M[N-K:]:
        print("NO")
    else:
        print("YES")