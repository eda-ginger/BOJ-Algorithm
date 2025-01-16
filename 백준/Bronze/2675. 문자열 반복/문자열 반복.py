n = int(input())
for i in range(n):
    r, a = map(str, input().split())
    sentence = ''
    for w in a:
        sentence += w*int(r)
    print(sentence)