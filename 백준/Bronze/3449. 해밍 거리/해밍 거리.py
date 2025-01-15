N = int(input())
for i in range(N):
    a = str(input())
    b = str(input())
    print(f'Hamming distance is {sum([c1 != c2 for c1, c2 in zip(a, b)])}.')    