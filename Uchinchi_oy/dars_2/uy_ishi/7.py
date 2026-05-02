n = int(input("N ni kiriting: "))
yigindi = 0
while n > 0:
    yigindi += n % 10
    n = n // 10
print(yigindi)
