N, D, P = map(int, input().split())
fares = list(map(int, input().split()))

sorted_fares = sorted(fares, reverse=True)

total_cost = sum(fares)

for i in range(0, N, D):
    savings = sum(sorted_fares[i:i+D]) - P
    if savings > 0:
        total_cost -= savings

print(total_cost)