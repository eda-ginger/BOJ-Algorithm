a = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
b = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
c = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]
t = ['t', 'f', 'f', 't', 'f', 'f', 't']

n = int(input())
for i in range(n):
    total = 0
    scores = list(map(int, input().split()))
    for idx, s in enumerate(scores):
        if t[idx] == 't':
            total += int(a[idx] * (b[idx] - s) ** c[idx])
        else:
            total += int(a[idx] * (s - b[idx]) ** c[idx])
    print(total)