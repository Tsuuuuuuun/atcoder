N,K = map(int,input().split())

A = []
B = []
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

zip_ab = zip(A,B)
zip_sort = sorted(zip_ab, key=lambda x:x[0])
A,B = zip(*zip_sort)

sum = sum(B)

if sum <= K:
    print(1)
else:
    for i in range(N):
        if sum <=K:
            print(A[i-1]+1)
            break
        sum -= B[i]
        if i == N-1:
            print(A[i]+1)