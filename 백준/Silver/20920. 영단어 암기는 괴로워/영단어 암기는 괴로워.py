# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

import sys
N, M = map(int, input().split())
data = [sys.stdin.readline().strip() for i in range(N)]

words = {}
for word in data:
    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word in sorted_words:
    print(word[0])
