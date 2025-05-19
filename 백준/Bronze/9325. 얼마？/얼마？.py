for _ in range(int(input())):
    car = int(input())
    qn = int(input())
    if qn:
        for _ in range(qn):
            q, p = map(int, input().split())
            car += q * p
    print(car)