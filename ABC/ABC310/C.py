N = int(input())
S = []

for _ in range(N):
    S.append(input())
unique_sticks = set()

for i in range(N):
    stick_id = min(S[i], S[i][::-1])

    unique_sticks.add(stick_id)

print(len(unique_sticks))