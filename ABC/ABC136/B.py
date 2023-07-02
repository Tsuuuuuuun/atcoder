N = int(input())

keta = len(str(N))

ans = None
if keta == 1:
    ans = N
if keta == 2:
    ans = 9
if keta == 3:
    ans = N-90
if keta == 4:
    ans = 909
if keta == 5:
    ans = N-9009
if keta == 6:
    ans = 90909

print(ans)