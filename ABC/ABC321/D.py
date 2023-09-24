import bisect
N,M,P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A)
sorted_B = sorted(B)
cumulative_sum_B = [0]
for b in sorted_B:
    cumulative_sum_B.append(cumulative_sum_B[-1] + b)
total_price = 0

for a in A:
    idx = bisect.bisect_left(sorted_B, P - a)
    total_price += cumulative_sum_B[idx] + a * idx + P * (M - idx)

print(total_price)
