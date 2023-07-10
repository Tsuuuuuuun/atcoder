N,M,H,K = map(int,input().split())
S = input()
items = set(tuple(map(int,input().split())) for _ in range(M))

ans = "Yes"
x,y = 0,0
for c in S:
    if c == 'R':
        x += 1
    elif c == 'L':
        x -= 1
    elif c == 'U':
        y += 1
    elif c == 'D':
        y -= 1
    
    H -= 1
    if H < 0:
        ans = "No"
        break
    if (x,y) in items and H < K:
        H = K
        items.remove((x,y))

print(ans)