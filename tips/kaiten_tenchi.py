# https://qiita.com/snhrhdt/items/e3651d787e33653d5538
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate = lambda A: [list(x)[::-1] for x in zip(*A)] 

rotate(A) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

transpose = lambda A: [list(x) for x in zip(*A)]

transpose(A) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
