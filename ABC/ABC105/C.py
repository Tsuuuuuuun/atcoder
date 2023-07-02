S = input()
K = int(input())

ans = None

if S[0] != 1:
    ans = S[0]

else:
    for i in range(min(len(S), K)):
        if S[i] != 1:
            ans = S[i]
            break


print(ans)