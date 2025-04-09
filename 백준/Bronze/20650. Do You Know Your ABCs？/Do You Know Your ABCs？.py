import itertools

def find_abc(l):
    m = max(l)
    ll = [i for i in l if i != m]
    for l in itertools.combinations(ll, 3):
        if m == sum(l):
            return ' '.join(map(str, sorted(l)))

lst = list(map(int, input().split()))
print(find_abc(lst))