import numpy as np
N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

hantei = "one"

for i in range(len(C)):
    if T == C[i]:
        hantei = "two"
        
if hantei == "one":
    score_list = []
    for i in range(len(C)):
        if C[i] == C[0]:
            score_list.append(R[i])
        else:
            score_list.append(0)
    print(np.argmax(score_list) + 1)
    
if hantei == "two":
    score_list = []
    for i in range(len(C)):
        if C[i] == T:
            score_list.append(R[i])
        else:
            score_list.append(0)
    print(np.argmax(score_list) + 1)