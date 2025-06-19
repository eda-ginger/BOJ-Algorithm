def xor_repeat(A, B, C):
    return A if C % 2 == 0 else A ^ B

a, b, c = map(int, input().split())
print(xor_repeat(a, b, c))