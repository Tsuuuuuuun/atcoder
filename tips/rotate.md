
# rotate

pythonでリストを回転させる方法

## 1. zipを使う

```python
A=[list(a)[::-1] for a in zip(*A)]
```

## 2. numpyを使う

```python
import numpy as np
A=np.rot90(A)
```
