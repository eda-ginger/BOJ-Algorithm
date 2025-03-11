s = input()
result = []
for i in s:
    if i.islower():
        result.append(i.upper())
    else:
        result.append(i.lower())
print(''.join(result))