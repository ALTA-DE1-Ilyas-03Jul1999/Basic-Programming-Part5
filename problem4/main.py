def muncul_sekali(angka):
    counts = {} 
    for num in angka:
        num_int = int(num)
        if num_int in counts:
            counts[num_int] += 1
        else:
            counts[num_int] = 1

    return [key for key, value in counts.items() if value == 1]


if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]