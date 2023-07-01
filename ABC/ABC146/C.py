A,B,X = map(int, input().split())

def is_ok(mid):
    if (A * mid) + (B * len(str(mid))) <= X:
        return True
    else:
        return False


def binary_search(ok,ng):
    while ng-ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok =  mid
        else:
            ng = mid
    
    return ok
    
ans = binary_search(0, 10 ** 9 + 1)
print(ans)