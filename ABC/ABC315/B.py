M = int(input())
D = list(map(int, input().split()))
total_days = sum(D)
middle_day = (total_days + 1) // 2
current_day = 0
for month, days_in_month in enumerate(D, start=1):
    current_day += days_in_month
    if current_day >= middle_day:
        day_in_month = middle_day - (current_day - days_in_month)
        result_month = month
        result_day = day_in_month
        break

print(result_month, result_day)
