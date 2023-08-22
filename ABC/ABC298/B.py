N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
B = []
for i in range(N):
    B.append(list(map(int, input().split())))

rotate = lambda A: [list(x)[::-1] for x in zip(*A)] 

ans = "No"

for _ in range(4):
    flg = False
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                continue
            if A[i][j] != B[i][j]:
                flg = True
                break
        if flg:
            break
    if not flg:
        ans = "Yes"
        break
    A = rotate(A)

print(ans)