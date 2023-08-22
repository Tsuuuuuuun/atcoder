S = input()
ans = "Yes"
B_pos = [i for i, char in enumerate(S) if char == "B"]

if B_pos[0] % 2 == B_pos[1] % 2:
    ans = "No"

R_pos = [i for i, char in enumerate(S) if char == "R"]
K_pos = S.index("K")

if not (R_pos[0] < K_pos < R_pos[1]):
    ans = "No"
    
print(ans)