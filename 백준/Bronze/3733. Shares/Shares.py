while True:
    try:
        N, S = map(int, input().split())
        result = S // (N+1)
        print(result)
    except:
        break