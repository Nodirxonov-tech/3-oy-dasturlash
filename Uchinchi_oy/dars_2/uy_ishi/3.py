a=int(input("A ni kiriting: "))
b = int(input("B ni kiriting: "))
yigindi=0
for i in range(a, b+1):
    if i%2==0:
        yigindi+=i
print(yigindi)