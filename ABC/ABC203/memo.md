
# A

問題文を読んだまま.  三項演算子を使うと短く書ける.

```python
a,b,c=sorted(input().split())
print(c if a==b else a if b==c else 0)
```

# B

forで足すだけ.

# C

愚直な足し合わせで計算すると $O(N^2)$ になってしまう. $i=1,2,\cdots N$ について昇順に $K+B_i + \cdots B_{i-1} \leq A_i$ かどうかを調べる.
