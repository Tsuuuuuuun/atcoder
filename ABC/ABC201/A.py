A = list(map(int, input().split()))
A.sort()
ans = "Yes" if A[2] - 2* A[1] + A[0] == 0 else "No"
print(ans)