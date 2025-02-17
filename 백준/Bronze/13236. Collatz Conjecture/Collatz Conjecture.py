n = int(input())
steps = [str(n)]
while n != 1:
    if n % 2 == 0:
        n /= 2
        steps.append(str(int(n)))
    else:
        n = n*3 + 1
        steps.append(str(int(n)))
print(' '.join(steps))
