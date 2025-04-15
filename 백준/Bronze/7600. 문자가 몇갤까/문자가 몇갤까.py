import string
d = dict.fromkeys(string.ascii_lowercase, 0)

while True:
    sentence = input().lower()
    if sentence == '#':
        break
    count_alpha = set([s for s in sentence if s in d])
    print(len(count_alpha))
