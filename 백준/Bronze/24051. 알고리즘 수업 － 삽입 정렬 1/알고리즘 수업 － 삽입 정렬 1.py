def insertion_sort(N, K, A):
    count = 0
    for i in range(1, N):
        loc = i - 1
        newItem = A[i]

        while loc >= 0 and newItem < A[loc]:
            A[loc + 1] = A[loc]
            count += 1
            if count == K:
                return A[loc + 1]
            loc -= 1

        if loc + 1 != i:
            A[loc + 1] = newItem
            count += 1
            if count == K:
                return A[loc + 1]
    return -1

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(insertion_sort(n, k, a))