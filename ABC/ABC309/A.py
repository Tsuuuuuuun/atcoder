adjacent_pairs = [(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 9)]

A,B =map(int, input().split())
ans = "No"
for pairs in adjacent_pairs:
    if (A,B) == pairs:
        ans = "Yes"
print(ans)
