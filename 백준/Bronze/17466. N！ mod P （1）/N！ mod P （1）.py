n, p = map(int, input().split())

def factorial_mod(n, p):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % p
    return result

print(factorial_mod(n, p))