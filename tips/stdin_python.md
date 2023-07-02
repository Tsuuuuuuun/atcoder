
# abst

Pythonの標準入力についてのメモ. これまではネットにあるやつを参考にしていたけど, しばしば網羅されてなかったりしたのでそれも含めて遭遇したものをメモる. ターミナル上でテストケースを回すためになるべく1行ごとに入力されるのが望ましい.

# 1行1列

入力がstrのとき
> $s$

```Python
s = input()
```

入力がintのとき

>$n$

```Python
n = int(input())
```

>$a$

入力がfloatのとき

```Python
a = float(input())
```

# 1行n列

入力を書く変数で受け取るとき

> $A,B,C$

strの場合

```Python
A,B = input().split
```

intの場合

```Python
A, B = map(int, input().split())
```

入力をリストで受け取りたいとき

> $A_1, A_2, ... ,A_n$

strの場合

```Python
A = input().split
```

intの場合

```Python
A = list(map(int,input().split()))
```

# n行m列

列に変数が並ぶ場合

```text
N
x1 y1
x2 y2
:
xN yN
```

```Python
N = int(input())
x = [None]*N
y = [None*N]

for i in range(N):
    x[i], y[i] = map(int,input().split())
```

# 一般行列データ

入力

```text
N M
A1,1 A1,2 ... A1,N
:
AM,1 AM,2 ... AM,N
```

```Python
N,M = map(int, input().split())
A = []
for i in range(M):
    a = list(map(int, input().split()))
    A.append(a)
```

1文字ずつ取得したい場合(例: <https://atcoder.jp/contests/abc300/tasks/abc300_b>)

```Python
H,W = map(int, input().split())
A = []
B = []
for _ in range(H):
    row = list(input())
    A.append(row)
 
for _ in range(H):
    row = list(input())
    B.append(row)
```
