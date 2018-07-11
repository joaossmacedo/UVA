def no_of_possibilities(n):
    a = 0
    b = 1

    for i in range(n):
        temp = b
        b = b + a
        a = temp

    return b


while True:
    n = int(input())
    if n == 0:
        break

    print(no_of_possibilities(int(n)))
