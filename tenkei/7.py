from bisect import bisect_left

N = int(input())
A = list(map(int,input().split()))

Q = int(input())
B = [int(input()) for _ in range(Q)]
A.sort()

for i in range(Q):
    x = bisect_left(A,B[i])
    if x == 0:
        print(A[0]-B[i])
    elif x == N:
        print(B[i] - A[-1])
    else:
        print(min(B[i] - A[x-1], A[x] - B[i]))