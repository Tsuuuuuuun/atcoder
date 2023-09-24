N = int(input())
N_str = str(N)
ans = "Yes"
for i in range(1, len(N_str)):
    if N_str[i - 1] <= N_str[i]:
        ans = "No"
print(ans)
