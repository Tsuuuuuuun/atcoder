N = int(input())
X = list(map(int, input().split()))
sum_list = []
for i in range(min(X), max(X) +1):
    sum = 0
    for j in range(len(X)):
        sum += (X[j]-i) **2
    
    sum_list.append(sum)

print(min(sum_list))