from itertools import permutations

def check_string_rearrangement(N, M, strings):
    for perm in permutations(strings):
        for i in range(len(perm) - 1):
            count = sum(1 for a, b in zip(perm[i], perm[i+1]) if a != b)
            if count > 1:
                break
        else:
            return "Yes"

    return "No"


# 入力の読み込み
N, M = map(int, input().split())
strings = []
for _ in range(N):
    s = input()
    strings.append(s)

# 条件を満たすか判定
result = check_string_rearrangement(N, M, strings)
print(result)
