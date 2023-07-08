N, D = map(int, input().split())
T = list(map(int, input().split()))

ans = False
for i in range(N-1):
    if T[i+1] - T[i] <= D:
        print(T[i+1])
        ans = True
        break

if not ans:
    print(-1)