
t = int(input())

for i in range(t):
    n = int(input())
    p = int(input())

    hartals = []

    for j in range(p):
        hartals.append(int(input()))

    days = []

    for j in range(1, n + 1):
        day_lost = False

        if not (j % 7 == 6 or j % 7 == 0):
            for k in range(len(hartals)):
                if j % hartals[k] == 0:
                    day_lost = True
                    break

        days.append(day_lost)

    print(days.count(True))
