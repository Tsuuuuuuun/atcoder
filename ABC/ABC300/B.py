H,W = map(int, input().split())
A = list(input())
B = list(input())
ans = "No"

for s in range(H):
    for t in range(W):
        A_move = [[None]*W]*H
        for ss in range(H):
            for tt in range(W):
                A_move[ss][tt] = A[(ss+s+1)%H][(tt+t+1)%W]
        if A_move == B:
            ans = "Yes"

print(ans)