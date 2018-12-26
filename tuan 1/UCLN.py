def UCLN (a, b):
    if a == b:
        return a;
    elif abs(a - b) == 1:
        return 1
    else:
        if a > b:
            return UCLN(b, a - b)
        else:
            return UCLN(a, b - a)



print(UCLN(10, 30))
