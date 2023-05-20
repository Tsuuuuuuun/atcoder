# 入力の取得
A, B = map(int, input().split())


# 敵の体力が0以下になるまで攻撃を繰り返す

if A % B == 0:
  attack_count = A // B
else:
  attack_count = A//B + 1

# 結果の出力
print(attack_count)