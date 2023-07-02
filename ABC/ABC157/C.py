N,M = map(int,input().split())
s = [None]*M
c = [None]*M
for i in range(M):
    s[i], c[i] = map(int,input().split())
ans = ['a']*N

for i in range(M):
    if ans != -1 and ans[s[i]-1] == 'a':
        ans[s[i]-1] = str(c[i])
    elif ans[s[i]-1] != str(c[i]):
        ans = -1
        break

if ans == -1:
    print(-1)

elif M ==0:
    if N == 1:
        print(0)
    if N == 2:
        print(10)
    if N == 3:
        print(100)

elif ans[0] == '0' and N != 1:
    print(-1)

else:
    for i in range(N):
        if ans[i] == 'a':
            if i == 0:
                ans[i] = '1'
            else:
                ans[i] = '0'
        print(ans[i], end="")