#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력
A, B, C = map(int, input().split())
print(f"{(A+B)%C}\n{((A%C) + (B%C))%C}\n{(A*B)%C}\n{((A%C)*(B%C))%C}")