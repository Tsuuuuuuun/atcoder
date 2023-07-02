N = int(input())
S = []
for i in range(N):
    S.append(input())

ans = "No"

for i in range(N):
    for j in range(N):
        if i != j:
            text = S[i] + S[j]
            if text == text[::-1]:
                ans = "Yes"

print(ans)