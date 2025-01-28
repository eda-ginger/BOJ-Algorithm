n = int(input())
line = str(input())
int2 = line.count('2')
str2 = line.count('e')
if int2 == str2:
    print('yee')
elif int2 > str2:
    print('2')
else:
    print('e')