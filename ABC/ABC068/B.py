N = int(input())

ans = 1
max_cnt = 0
for i in range(1,N+1):
    tmp_i = i
    cnt = 0
    while tmp_i % 2 == 0:
        cnt += 1
        tmp_i = tmp_i // 2
    if cnt > max_cnt:
        ans = i
        max_cnt = cnt


print(ans)