N = int(input())
A = list(map(int, input().split()))
middle_indices = {}
occurrence_counts = {}

for i in range(len(A)):
    if A[i] not in occurrence_counts:
        occurrence_counts[A[i]] = 1
    else:
        occurrence_counts[A[i]] += 1
        
    if occurrence_counts[A[i]] == 2:
        middle_indices[A[i]] = i

sorted_numbers = sorted(middle_indices, key=middle_indices.get)
for i in range(len(sorted_numbers)):
    print(sorted_numbers[i], end = " ")
