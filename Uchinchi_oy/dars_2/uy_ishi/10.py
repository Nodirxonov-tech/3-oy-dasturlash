n=int(input("N ni kiriting: "))
while n!=1 and n!=4:
    yigindi=0
    temp=n
    
    while temp>0:
        raqam=temp%10
        yigindi+=raqam**2
        temp //= 10

    n=yigindi

if n==1:
    print(True)
else:
    print(False)