A = []
for i in range(3):
    a = list(map(int, input().split()))
    A.append(a)

N = int(input())
b = []
for i in range(N):
    b.append(int(input()))

for i in range(N):
    for j in range(3):
        for k in range(3):
            if A[k][j] == b[i]:
                A[k][j] = 0

ans = "No"

if A[0] == [0,0,0]:
    ans = "Yes"

if A[1] == [0,0,0]:
    ans = "Yes"

if A[2] == [0,0,0]:
    ans = "Yes"

for i in range(3):
    if A[0][i] == 0 and A[1][i] == 0 and A[2][i] == 0:
        ans = "Yes"

if A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
    ans = "Yes"

if A[2][0] == 0 and A[1][1] == 0 and A[0][2] == 0:
    ans = "Yes"

print(ans)
