N,M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))
P0 = P[0]
Prices = P[1:]

color_price = dict(zip(D, Prices))
total = 0
for plate in C:
    if plate in color_price:
        total += color_price[plate]
    else:
        total += P0

print(total)