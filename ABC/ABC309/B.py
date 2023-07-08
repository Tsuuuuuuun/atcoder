def rotate_matrix(n, matrix):
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 上の行を右に移動
            if i == 0 and j < n-1:
                rotated[i][j+1] = matrix[i][j]
            # 右の列を下に移動
            elif j == n-1 and i < n-1:
                rotated[i+1][j] = matrix[i][j]
            # 下の行を左に移動
            elif i == n-1 and j > 0:
                rotated[i][j-1] = matrix[i][j]
            # 左の列を上に移動
            elif j == 0 and i > 0:
                rotated[i-1][j] = matrix[i][j]
            # 内部のマスはそのまま
            else:
                rotated[i][j] = matrix[i][j]
    return rotated

n = int(input())
A = []
for i in range(n):
    row = list((input()))
    A.append(row)

rotate_A = rotate_matrix(n, A)
for i in range(n):
    for j in range(n):
        if j < n-1:
            print(rotate_A[i][j], end = "")
        else:
            print(rotate_A[i][j])
