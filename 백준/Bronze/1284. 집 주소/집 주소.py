while True:
    n = input()
    if n == '0':
        break
    else:
        total = len(n) + 1
        for i in n:
            if int(i) == 0:
                total += 4
            elif int(i) == 1:
                total += 2
            else:
                total += 3
        print(total)