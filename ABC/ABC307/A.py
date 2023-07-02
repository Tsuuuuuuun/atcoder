N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    sum = 0
    for j in range(7):
        sum += A[7*i + j]
    print(sum, end=" ")