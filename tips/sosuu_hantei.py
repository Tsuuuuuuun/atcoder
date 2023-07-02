def eratosthenes(n):
    # n までの自然数を列挙する
    isPrimes = [True] * (n+1)

    # 0 と 1 を取り除く
    isPrimes[0], isPrimes[1] = False, False

    # 2 から √n まで繰り返す
    for i in range(2, int(n**0.5)+1):
        # i が取り除かれていないとき
        if isPrimes[i]:
            # i の倍数を取り除く
            for j in range(2*i, n+1, i):
                isPrimes[j] = False

    # 2 から n までの素数のリストを返す
    return [i for i in range(2, n+1) if isPrimes[i]]