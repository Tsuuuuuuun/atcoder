# incomplete

W,H = map(int,input().split())
N = int(input())
p = []
q = []

for i in range(N):
    x,y = map(int,input().split())
    p.append(x)
    q.append(y)

A = int(input())
a = list(map(int,input().split()))
B = int(input())
b = list(map(int,input().split()))

a.append(W)
b.append(H)

