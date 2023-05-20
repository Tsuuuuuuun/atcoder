H, W = map(int, input().split())
A = [list(map(int, input().split())) for l in range(H)]
B = [[0] * W for _ in range(H)]

row_sum = [0]*H
column_sum = [0]*W


for i in range(H):
    for j in range(W):
        row_sum[i] += A[i][j]

for i in range(W):
    for j in range(H):
        column_sum[i] += A[j][i]

for i in range(H):
    for j in range(W):
        B[i][j] = row_sum[i] + column_sum[j] - A[i][j]

for i in range(H):
    for j in range(W):
        print(int(B[i][j]), end = " ")
    print("")