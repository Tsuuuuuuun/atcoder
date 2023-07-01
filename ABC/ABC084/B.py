A,B = map(int,input().split())
S = input()
ans = "Yes"
for i in range(len(S)):
    if i < A:
        if not S[i].isdecimal():
            ans = "No"
    if i == A:
        if S[i].isdecimal():
            ans = "No"
    if i > A:
        if not S[i].isdecimal():
            ans = "No"

print(ans)