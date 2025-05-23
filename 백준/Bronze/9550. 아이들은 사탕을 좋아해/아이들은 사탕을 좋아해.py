for _ in range(int(input())):
    baby = 0
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    for c in candy:
        baby += c // k
    print(baby)
    
