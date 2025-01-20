word = str(input())
for c in range(97,123):
    cc = chr(c)
    if cc in word:
        if c == 122:
            print(word.index(cc))
        else:
            print(word.index(cc), end=' ')
    else:
        if c == 122:
            print(-1)
        else:
            print(-1, end=' ')
