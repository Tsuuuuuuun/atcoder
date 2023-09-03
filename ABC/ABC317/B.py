N = int(input())
A = list(map(int, input().split()))
def find_missing_number(N, A):
    A.sort()

    for i in range(A[0], A[-1] + 1):
        if i not in A:
            return i
    return A[0] - 1 if A[0] - 1 not in A else A[-1] + 1
print(find_missing_number(N, A))
