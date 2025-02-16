from collections import Counter

def anagram_distance(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    
    total_diff = 0
    
    # a에 있는 문자 기준으로 차이 계산
    for char in count_a:
        total_diff += abs(count_a[char] - count_b.get(char, 0))
    
    # b에 있는 문자 기준으로 차이 계산 (이미 처리한 문자는 제외)
    for char in count_b:
        if char not in count_a:
            total_diff += count_b[char]
    
    return total_diff

n = int(input())
for i in range(n):
    a = input().strip()
    b = input().strip()
    
    result = anagram_distance(a, b)
    
    print(f'Case #{i+1}: {result}')
