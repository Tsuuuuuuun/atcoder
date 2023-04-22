n = int(input()) 
s = input()
bar = []
ans = "out"

for i in range(n):
    if s[i] == '*':
        apo = i
    elif s[i] == '|':
        bar.append(i)

if bar[0] < apo and apo < bar[1]:
    ans = 'in'

print(ans)