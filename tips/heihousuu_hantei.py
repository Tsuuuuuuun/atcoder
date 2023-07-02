def isRationalNumber(number):
    result = False
    if number==1:
        return True
    for i in range(2,number):
        if number==i**2:
            return True
    return result