N = int(input())
dishes = [list(map(int, input().split())) for l in range(N)]

dp = [[-1 for _ in range(2)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    X = dishes[i][0]
    Y = dishes[i][1]
    for j in range(2):
        if dp[i][j] == -1:
            continue
        dp[i+1][j] = max([dp[i+1][j], dp[i][j]])
        if j == 0 or X == 0:
            dp[i+1][X]= max(dp[i+1][X], dp[i][j] + Y)

print(max(dp[N]))