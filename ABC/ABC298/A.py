N = int(input())
S = input()

x_cnt = 0
o_cnt = 0
for i in range(N):
    if S[i] == 'x':
        x_cnt += 1
    if S[i] == 'o':
        o_cnt += 1

if x_cnt == 0 and o_cnt >= 1:
    print("Yes")

else:
    print("No")
