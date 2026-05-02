n=int(input("N ni kiriting: "))
temp=n
teskari=0
while temp>0:
    qoldiq=temp%10
    teskari=(teskari*10)+qoldiq
    temp=temp//10

if n==teskari:
    print(True)
else:
    print(False)