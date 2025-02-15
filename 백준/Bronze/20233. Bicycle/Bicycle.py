a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

A = a + max(t-30, 0)*x*21
B = b + max(t-45, 0)*y*21
print(A, B)