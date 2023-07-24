N, K = map(int, input().split())
AB = []

for i in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

AB.sort(key=lambda x: x[0])

for i in range(N):
    if AB[i][0] > K:
        break
    K += AB[i][1]
print(K)