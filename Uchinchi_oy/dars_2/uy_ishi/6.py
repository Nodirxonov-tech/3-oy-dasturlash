n = int(input("N ni kiriting: "))

for i in range(2, n + 1):

    tub=True

    for u in range(2, i):

        if i % u == 0:
            tub=False
            break

    if tub:
        print(i, end=" ")
