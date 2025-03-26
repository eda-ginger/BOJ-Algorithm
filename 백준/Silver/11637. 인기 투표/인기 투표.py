t = int(input())
for _ in range(t):
    nn = int(input())
    human = []
    for _ in range(nn):
        sc = int(input())
        human.append(sc)
    mx = max(human)
    idx = human.index(mx)
    if human.count(mx) >= 2:
        print("no winner")
    else:
        if mx <= sum(human) / 2:
            print(f"minority winner {idx+1}")
        else:
            print(f"majority winner {idx+1}")