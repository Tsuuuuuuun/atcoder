MOD = 998244353

S = input()
n = len(S)
dp = [[0] * (n+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if S[i] == '(':
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
        elif S[i] == ')':
            if j > 0:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= MOD
        else:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD
            if j > 0:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= MOD
                    

print(dp[n][0])