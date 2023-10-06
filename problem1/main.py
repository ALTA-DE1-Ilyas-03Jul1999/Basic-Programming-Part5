def prime_number(number):
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= number:
        if number % i == 0:
            return False

        i += w
        w = 6-w

    return True

if __name__ == '__main__':
    print(prime_number(1000000007))  # True
    print(prime_number(1500450271))  # True
    print(prime_number(1000000000))  # False
    print(prime_number(10000000019))  # True
    print(prime_number(10000000033))  # True

