a, b, c = map(int, input().split())
alpha = ['A', 'B', 'C']
alpha_lst = [a, b, c]
if a == b == c == 0 or a == b == c == 1:
    print('*')
else:
    count1 = [a, b, c].count(0)
    count2 = [a, b, c].count(1)
    if count1 < count2:
        print(alpha[alpha_lst.index(0)])
    else:
        print(alpha[alpha_lst.index(1)])