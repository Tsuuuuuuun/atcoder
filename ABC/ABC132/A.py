s = sorted(input())

ans = "No"
if s[0] == s[1] and s[2] == s[3] and s[1] != s[2]:
    ans = "Yes"

print(ans)