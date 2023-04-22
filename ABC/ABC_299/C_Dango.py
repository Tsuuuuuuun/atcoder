N = int(input())
S = input()

bar = [-1]
for i in range(N):
    if S[i] == "-":
        bar.append(i)
bar.append(N)
bar_diff = []
for i in range(1, len(bar)):
    bar_diff.append(bar[i] - bar[i-1] - 1)

if len(bar) == N+2 or len(bar) == 2:
    ans = -1
else:
    ans = max(bar_diff)
print(ans)
