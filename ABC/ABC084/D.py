# RE
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

Q = int(input())
l = [None]*Q
r = [None]*Q
for i in range(Q):
    l[i],r[i] = map(int,input().split())

S = [0]*10002

for i in range(10001):
    if is_prime(i) and is_prime((i+1)//2):
        S[i] += 1

ans = [0]*10002
for i in range(10001):
    ans[i+1] = ans[i] + S[i]

for i in range(Q):
    print(ans[r[i]+1]-ans[l[i]])
