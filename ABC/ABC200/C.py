N = int(input())
A = list(map(int,input().split()))
A_amari = [0] * 200
ans = 0
for i in range(N):
    A_amari[A[i]%200] += 1

for i in range(200):
    ans += A_amari[i] * (A_amari[i]-1) // 2

print(ans)