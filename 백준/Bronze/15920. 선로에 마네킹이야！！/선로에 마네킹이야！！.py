flag = 0
cnt = 0

n = int(input())
str_input = input()

for i in str_input:
    if i == 'W':
        cnt += 1
    else:
        if cnt == 1:
            flag = 2
        elif cnt == 0 and flag == 0:
            flag = 1
        elif cnt == 0 and flag == 1:
            flag = 0

if cnt >= 2:
    if flag == 0:
        print(5)
    elif flag == 1:
        print(1)
    else:
        print(6)
else:
    print(0)
