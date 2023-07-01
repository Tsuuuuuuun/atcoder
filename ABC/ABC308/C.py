from decimal import Decimal # https://docs.python.org/ja/3/library/decimal.html
N = int(input())
A = [None]*N
B = [None]*N
for i in range(N):
    A[i],B[i] = map(Decimal,input().split())

success_rates = [(A[i] / (A[i] + B[i]), i + 1) for i in range(N)]
success_rates.sort(key=lambda x: (-x[0], x[1]))

for i in range(len(success_rates)):
    print(success_rates[i][1], end=" ")