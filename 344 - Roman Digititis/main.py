def define_i(n: int):
    r = 0
    dozens = int(n / 10)

    r += dozens * 14

    i = n % 10

    if i == 1:
        r += 1
    elif i == 2:
        r += 3
    elif i == 3:
        r += 6
    elif i == 4:
        r += 7
    elif i == 5:
        r += 7
    elif i == 6:
        r += 8
    elif i == 7:
        r += 10
    elif i == 8:
        r += 13
    elif i == 9:
        r += 14

    return r


def define_v(n: int):
    r = 0
    dozens = int(n / 10)

    r += dozens * 5

    i = n % 10

    if i == 4:
        r += 1
    elif i == 5:
        r += 2
    elif i == 6:
        r += 3
    elif i == 7:
        r += 4
    elif i >= 8:
        r += 5

    return r


def define_x(n: int):
    r = 0

    if n == 100:
        r = 150
    elif n >= 90:
        r = 140 + (n % 10)
    elif n >= 80:
        r = 111 + ((n % 10) * 3)
    elif n >= 70:
        r = 89 + ((n % 10) * 2)
    elif n >= 60:
        r = 77 + (n % 10)
    elif n >= 50:
        r = 75
    elif n >= 40:
        r = 65 + (n % 10)
    elif n >= 30:
        r = 36 + ((n % 10) * 3)
    elif n >= 20:
        r = 14 + ((n % 10) * 2)
    elif n >= 10:
        r = 2 + (n % 10)
    else:
        r = 0

    if n % 10 == 9:
        r += 1

    return r


# this function has an upper case L because a lower case L can be confused with an upper case I
def define_L(n: int):
    r = 0
    if n < 40:
        r = 0
    elif n < 90:
        r = n - 39
    else:
        r = 50

    return r


def define_c(n: int):
    r = 0
    if n < 90:
        r = 0
    else:
        r = n - 89

    return r


while True:
    value = int(input())
    if value == 0:
        break
    i = define_i(value)
    v = define_v(value)
    x = define_x(value)
    # this variable is upper case because a lower case L can be confused with an upper case I
    L = define_L(value)
    c = define_c(value)

    print(str(value) + ': ' + str(i) + ' i, ' + str(v) + ' v, ' + str(x) + ' x, ' + str(L) + ' l, ' + str(c) + ' c')
