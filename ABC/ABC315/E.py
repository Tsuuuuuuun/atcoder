import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

N = int(input().strip())
books_info = [tuple(map(int, input().strip().split())) for _ in range(N)]

graph_correct = defaultdict(list)
for i, info in enumerate(books_info):
    C = info[0]
    prerequisites = info[1:]
    for prerequisite in prerequisites:
        graph_correct[i + 1].append(prerequisite)

visited = [False] * (N + 1)
order_correct = []

def dfs_correct(book):
    if visited[book]:
        return
    visited[book] = True
    for dependent_book in graph_correct[book]:
        dfs_correct(dependent_book)
    order_correct.append(book)

dfs_correct(1)
order_correct = order_correct[:-1]

print(*order_correct)
