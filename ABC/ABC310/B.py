N,M = map(int,input().split())
ans = "No"
P = []
Q = []
F = []

for _ in range(N):
    pcf_list = list(map(int,input().split()))
    P.append(pcf_list[0])
    Q.append(pcf_list[1])
    F.append(pcf_list[2:])


for i in range(N):
    for j in range(N):
        if i != j:
            
            if P[i] < P[j]:
                continue
                
            if not set(F[i]) <= (set(F[j])):
                continue
    
            if P[i] > P[j] or len(set(F[j]).difference(set(F[i]))) > 0:
                ans = "Yes"

print(ans)