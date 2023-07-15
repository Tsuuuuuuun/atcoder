N,P,Q = map(int,input().split())
D = list(map(int,input().split()))
cost_without_coupon = P
cost_with_coupon = Q + min(D)

print(min(cost_without_coupon, cost_with_coupon))