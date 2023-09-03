N = int(input())

rectangles = [tuple(map(int, input().split())) for _ in range(N)]


grid = [[0] * 101 for _ in range(101)]

for rect in rectangles:
    A, B, C, D = rect
    for i in range(A, B):
        for j in range(C, D):
            grid[i][j] = 1

area = sum(row.count(1) for row in grid)
print(area)


