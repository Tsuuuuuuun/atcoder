N,L = map(int, input().split())
K = int(input())
A = list(map(int,input().split()))
A.append(L)
dif = [A[0]]
for i in range(N):
    dif.append(a[i+1]-a[i])

def is_ok(x):
    length = 0
    cnt = 0
    for i in dif:
        length += i
        if length >=x:
            length = 0
            cnt += 1
    return cnt

def meguru_bisect(ng, ok):
    while ng-ok > 1:
        mid = (ng - ok) //2
        if is_ok(mid) >= K+1:
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(L + 1, -1))
