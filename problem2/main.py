def pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        y = pow(x, n // 2)
        return y * y
    else:
        y = pow(x, (n - 1) // 2)
        return y * y * x


if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125