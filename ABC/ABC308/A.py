S = list(map(int,input().split()))
ans = "Yes"
for i in range(1,8):
    if S[i] - S[i-1] < 0:
        ans = "No"

for i in range(8):
    if S[i] % 25 != 0:
        ans = "No"
    if S[i] < 100 or S[i] > 675:
        ans = "No"

print(ans)