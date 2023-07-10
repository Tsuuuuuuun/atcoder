N = int(input())
S = []
A  = []
for i in range(N):
    s,a = input().split()
    S.append(s)
    A.append(int(a))

argmin = A.index(min(A))

for i in range(N):
    print(S[(argmin + i)%N])