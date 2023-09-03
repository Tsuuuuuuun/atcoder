N, M, P = map(int, input().split())
count = 0

for day in range(M, N + 1, P):
    count += 1

print(count)
