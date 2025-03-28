n = int(input())
for _ in range(n):
    lst = sorted(list(map(int, input().split())), reverse=True)
    ma, mi = lst[0], lst[-1]
    remain_lst = lst[1:-1]
    if remain_lst[0] - remain_lst[-1] >= 4:
        print('KIN')
    else:
        print(sum(remain_lst))
    