# coding: utf-8
# Your code here!

# マス目のサイズを取得
H, W = map(int, input().split())

# マス目の情報を取得
S = []
for _ in range(H):
    row = input()
    S.append(row)

# s, n, u, k, e の連続するマスを探索する
for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            # 縦方向の連続するマスを確認
            if i + 4 < H and S[i+1][j] == 'n' and S[i+2][j] == 'u' and S[i+3][j] == 'k' and S[i+4][j] == 'e':
                for k in range(5):
                    print(i+1+k, j+1)
                break
            
            # 横方向の連続するマスを確認
            if j + 4 < W and S[i][j+1] == 'n' and S[i][j+2] == 'u' and S[i][j+3] == 'k' and S[i][j+4] == 'e':
                for k in range(5):
                    print(i+1, j+1+k)
                break
            
            
            # 右斜め下方向の連続するマスを確認
            if i + 4 < H and j + 4 < W and S[i+1][j+1] == 'n' and S[i+2][j+2] == 'u' and S[i+3][j+3] == 'k' and S[i+4][j+4] == 'e':
                for k in range(5):
                    print(i+1+k, j+1+k)
                break
            # 左斜め下方向の連続するマスを確認
            if i + 4 < H and j - 4 >= 0 and S[i+1][j-1] == 'n' and S[i+2][j-2] == 'u' and S[i+3][j-3] == 'k' and S[i+4][j-4] == 'e':
                for k in range(5):
                    print(i+1+k, j+1-k)
                break
        elif S[i][j] == 'e':
            if i + 4 < H and S[i+1][j] == 'k' and S[i+2][j] == 'u' and S[i+3][j] == 'n' and S[i+4][j] == 's':
                for k in range(5):
                    print(i+5-k, j+1)
                break
            if j + 4 < W and S[i][j+1] == 'k' and S[i][j+2] == 'u' and S[i][j+3] == 'n' and S[i][j+4] == 's':
                for k in range(k):
                    print(i+1, j+5-k)
                break
            if i + 4 < H and j + 4 < W and S[i+1][j+1] == 'k' and S[i+2][j+2] == 'u' and S[i+3][j+3] == 'n' and S[i+4][j+4] == 's':
                for k in range(5):
                    print(i+5-k, j+5-k)
                break
            if i + 4 < H and j - 4 >= 0 and S[i+1][j-1] == 'k' and S[i+2][j-2] == 'u' and S[i+3][j-3] == 'n' and S[i+4][j-4] == 's':
                for k in range(5):
                    print(i+5-k, j-3+k)
                    
                break
