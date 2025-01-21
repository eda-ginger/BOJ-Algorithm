while True:
    try:
        l = list(map(int, input().split()))
        max_value = max(l)
        others = [x for x in l if x != max_value]

        if max_value**2 == others[0]**2 + others[1]**2:
            print("right")
        else:
            print("wrong")    
    except:
        break