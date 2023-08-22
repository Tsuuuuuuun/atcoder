from collections import defaultdict

N = int(input().strip())
ice_creams = [tuple(map(int, input().strip().split())) for _ in range(N)]

flavors_tastes = defaultdict(list)
for flavor, taste in ice_creams:
    flavors_tastes[flavor].append(taste)

max_satisfaction_same_flavor = 0
for tastes in flavors_tastes.values():
    tastes.sort(reverse=True)
    if len(tastes) > 1:
        satisfaction_same_flavor = tastes[0] + tastes[1] // 2
        max_satisfaction_same_flavor = max(max_satisfaction_same_flavor, satisfaction_same_flavor)

max_tastes = sorted([max(tastes) for tastes in flavors_tastes.values()], reverse=True)

max_satisfaction_different_flavors = 0
if len(max_tastes) > 1:
    max_satisfaction_different_flavors = max_tastes[0] + max_tastes[1]

final_max_satisfaction = max(max_satisfaction_different_flavors, max_satisfaction_same_flavor)

print(final_max_satisfaction)
