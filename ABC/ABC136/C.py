N = int(input())
H = list(map(int, input().split()))

ans = "Yes"

if N > 1:
    if H[0] > H[1] + 1:
        ans = "No"
    for i in range(1,N-1):
        if H[i] - 1 >= H[i-1]:
            H[i] -=1
        if H[i] > H[i+1]:
            ans = "No"

print(ans)