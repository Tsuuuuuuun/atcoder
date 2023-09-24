N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = -1
for i in range(101):
    scores = A + [i]
    scores.sort()
    if sum(scores[1:-1]) >= X:
        ans = i
        break
    
print(ans)