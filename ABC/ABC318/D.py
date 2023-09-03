def convert_input_to_matrix(N, edge_weights):
    D = [[0] * N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(i+1, N):
            D[i][j] = edge_weights[idx]
            D[j][i] = edge_weights[idx]
            idx += 1
    return D

def max_matching_weight(N, D):
    dp = [-float('inf')] * (1 << N)
    dp[0] = 0

    if N % 2 == 1:
        for i in range(N):
            dp[1 << i] = 0

    for mask in range(1 << N):
        for i in range(N):
            if not (mask & (1 << i)):
                continue
            for j in range(i + 1, N):
                if not (mask & (1 << j)):
                    continue
                prev_mask = mask ^ (1 << i) ^ (1 << j)
                dp[mask] = max(dp[mask], dp[prev_mask] + D[i][j])

    return dp[(1 << N) - 1]

N = int(input())
edge_weights = []
for _ in range(N - 1):
    edge_weights.extend(map(int, input().split()))
D = convert_input_to_matrix(N, edge_weights)
result = max_matching_weight(N, D)
print(result)