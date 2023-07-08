N,M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
sum_pool = sum(A)

if A[M-1] >= sum_pool/(4*M):
    print("Yes")
else:
    print("No")