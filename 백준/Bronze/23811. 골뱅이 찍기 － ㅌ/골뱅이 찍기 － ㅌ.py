n = int(input())
tn = ''
for i in range(3):
    tn += (('@'*n)*5 + '\n')*n
    
    if i != 2:
        tn += ('@'*n + '\n')*n

print(tn[:-1])