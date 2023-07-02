N = int(input())
S = input()
T = input()

ans = "Yes"

for i in range(N):
    if (S[i] == T[i]) or (S[i] == '1' and T[i] == 'l') or (T[i] == '1' and S[i] == 'l') or (S[i] == '0' and T[i] == 'o') or (T[i] == '0' and S[i] == 'o'):
        pass
    else:
        ans = "No"

print(ans)