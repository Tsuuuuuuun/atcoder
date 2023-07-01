# A
3つの条件を全て満たすかどうかの問題.

# B

料理の皿が値段に対応するということを考えると辞書で管理するのが妥当そう. インデックス($P_0$)の扱いに少し注意.

# C

成功率の高い順にソートしてインデックスを返せば良いと思ってそのまま提出したらエラーを吐かれた. 解説を見るに浮動小数点型の精度の問題があるとのこと. Pythonでの解決策はいくつかあり, 公式解説と同様にソートのキーを渡す場合は`cmp_to_key`関数を使って実装可能.
```Python
from functools import cmp_to_key
def cmp(a, b):
    x, y, i = a
    xx, yy, ii = b
    s = x * yy - y * xx
    return 1 if s > 0 else -1 if s < 0 else 0

N = int(input())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((-a, a + b, i))

X.sort(key = cmp_to_key(cmp))
print(*[i + 1 for x, y, i in X])

```
Pythonは多倍長整数が扱えるので, 十分な桁数を保持すれば良く, デカい数字(`10 ** 100`)をかければOK.

```Python
N = int(input())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((-a * 10 ** 100 // (a + b), i))

X.sort()
print(*[i + 1 for x, i in X])
```

Decimalを用いると浮動小数点より精度を上げることが可能だが, PyPyでは遅くなるらしい.