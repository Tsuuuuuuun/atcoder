N,M = map(int, input().split())
A = [list(map(int, input().split())) for l in range(M)]

tonari = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            tonari[i][j] = 1


for i in range(M):
    for j in range(N-1):
        tonari[A[i][j] - 1][A[i][j+1]-1] += 1
        tonari[A[i][j+1]-1][A[i][j]-1] += 1

cnt = 0
for i in range(N):
    for j in range(N):
        if tonari[i][j] == 0:
            cnt += 1

print(cnt // 2)