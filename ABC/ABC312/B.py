N, M = map(int, input().split())

grid = [input().strip() for _ in range(N)]

takcode = [
    "###.?????",
    "###.?????",
    "###.?????",
    "....?????",
    "?????????",
    "?????....",
    "?????.###",
    "?????.###",
    "?????.###"
]


def is_takcode(x, y):
    for i in range(4):
        for j in range(4):
            if grid[x+i][y+j] != takcode[i][j]:
                return False
    for i in range(5,9):
        for j in range(5,9):
            if grid[x+i][y+j] != takcode[i][j]:
                return False
    return True

ans = []
for i in range(N-8):
    for j in range(M-8):
        if is_takcode(i, j):
            ans.append((i+1, j+1))

for a in ans:
    print(a[0], a[1])
