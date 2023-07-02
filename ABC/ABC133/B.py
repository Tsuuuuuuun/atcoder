def isRationalNumber(number):
    result = False
    if number==1:
        return True
    for i in range(2,number):
        if number==i**2:
            return True
    return result

N, D = map(int, input().split())
X = []
for i in range(N):
    x = list(map(int, input().split()))
    X.append(x)

ans = 0

for i in range(N):
    for j in range(N):
        if i != j:
            length = 0
            for k in range(D):
                length += (X[i][k] - X[j][k]) ** 2
            if isRationalNumber(length):
                ans += 1

print(ans//2)