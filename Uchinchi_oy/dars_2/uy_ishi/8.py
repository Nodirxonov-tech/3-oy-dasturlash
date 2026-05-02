n=int(input("N ni kiriting: "))
kv_yigindi=0
while n>0:
    raqam=n%10
    kv_yigindi+=raqam**2
    n=n//10

print(kv_yigindi)