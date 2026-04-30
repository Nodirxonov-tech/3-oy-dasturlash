from 3-oy.1-dars.uy_ishi.15 import A

#### For va while masalalari.

## Oson masalalar.

# # 1-masala.

# for i in range(1, 500):  # for i in ...: Bu qism "har bir i soni uchun quyidagi ishni bajar" degan ma'noni anglatadi. range(1, 501): Bu funksiya 1 dan boshlab 500 gacha bo'lgan sonlarni tayyorlab beradi.
#     print(f"{i} ")

# # 2-masala.

# for i in range(250, -1, -1):  # 250 Tsikl aynan shu sondan boshlanadi. -1 qayerda toxtashini bildiradi. Keyingi -1 esa qadam har bitta aylanganda boshlangich son bitta kamayib boradi.
#     print(i)

# 3-masala.

# for i in range(530, 10, -1): #530 dan 10gacha aylanadi.
#     if i%2==0: # i soni juft ekanligini tekshiradi.
#         print(i)  # i agar juft bolsa ekranga i dagi qiyatlar chiqadi.

# # 4-masala.

# son=input("Natural son kiriting: ")  # Foydalanuvchi strin kiritadi.
# yigindi=0  # Ozgaruvchi kiritiba olamiz va unga 0 qiymat beramiz.
# for i in son:  # Bu sikl matndagi har bir raqamni bittalab oladi: avvala birinchi indeks dagi, keyin 2-indeksdagi va keyingi ideksdagi.
#     yigindi += int(i)  # Har bir yangi raqamni umumiy yani yigindi (savatga) qoshib boradi.

# print(yigindi)

# # 5-masala.
# n=int(input("son kiriting: "))
# yigindi=0
# for i in range(1, n):
#     if i%2==0:
#         yigindi+=(i)

# print(yigindi)

# # 6-masala.

# for i in range(ord('a'), ord('z'), +1):   # harflarni chiqarishda ASCII jadvalidan nechinchi raqm ekanligini ord() orqali yurgizamiz va i ni 1ga oshirib boramiz.
#     print(chr(i), end=(" "))  # chiqarishda i bizga ASCII dagi raqamini beradi biz uni chr() orqali harfga ogirib olamiz. va hardoim i dan keyin bosh joy qolishi va harfning orasida bosh joy qolishi uchun end() buyrugi ichiga (" ") bosh joy qoldiramiz.


## Orta masalalari.


# # 1-masala.

# n=int(input("son kiriting: "))

# yigindi=0

# for i in range(1, n, +1):
#     if n%i==0:
#         yigindi+=(i)

# if yigindi==n:
#     print("mukammal son")
# else:
#     print("mukammal son emas")


# # 2-masala.

# for i in range(100, 1000):
#     yuzlar=i//100
#     onlar=(i//10)%10
#     birlar=i%10

#     if (yuzlar==onlar) or (onlar==birlar) or (yuzlar==birlar):
#         print(i)

# # 3-masala.

# yigindi=0

# for i in range(1, 501, 2):
#         yigindi+=i

# yigindi_str=str(yigindi) # Chiqqan yigindini sondan stringga otkazamiz.

# # Yigindini stringga otkazib bolgach otkazgan string  yigindi_strni  palindiromi yoki yoqmi tekshiramiz.

# if yigindi_str==yigindi_str[::-1]:
#     print("True")
# else:
#     print("False")

# # 4-masala

# ## Shart:

# # Foydalanuvchidan N, M va K sonlarini qabul qiling. N dan M gacha K ta juft sonning yigindisini hisoblang.

# # Input N:2, M:10, K:3 .  Output: 12.

# n=int(input("N ni kiriting: "))  # boshlangich son.
# m = int(input("M ni kiriting: "))  # Shu songacha davom etadi
# k = int(input("K ni kiriting: ")) # Bu kiritlgan son sanoq . Yani shartda for siklida aylanganda ichidagin juft sonlarni sanash va chegara hisoblanadi.
# yigindi=0  # juft sonlarni yigindisini hisoblash uchun.
# count=0 coun sikl nechi marta aylanganini sanash uchun.

# for i in range(n, m+1):  # Sikl n dan m gacha aylanadi va mni ozini tashlab ketadi tashlab ketmasligi uchun +1 ni qoshamiz.
#     if i%2==0:  # i juft sonligini tekshirish sharti.
#         count+=1 # Sikl har aylanganda 1ni qoshadi.
#         yigindi+=i  # sikl har aylanganda shartni qanoatlantirsa yigindiga i ni qoshib ketadi.

#     if count==k: # count k ga teng bolganda sikl toxtaydi.
#         break

# print(yigindi) # sikl toxtaganda ekranga yigindini chiqaradi.


# 5-masala.

## Son va uning teskari soni orasidagi farq

## Shart:

## Foydalanuvchi natural son kiritadi. Shu son va shu sonning teskarisi orasidagi farqni aniqlang.

## Input 1:  Son: 12     Output 1: -9

## Input 2:  Son: 8   Output 2:   0

# son = int(input("natural son kiriting: "))
# temp_son=son  # Sonning nusxasini olamiz, chunki son o'zgaruvchisi tsikl davomida 0 bo'lib qoladi.
# teskari_son = 0
# while temp_son > 0:
#     qoldiq = temp_son % 10  # Oxirgi raqamni ajratib olamiz.
#     teskari_son = (teskari_son * 10) + qoldiq
#     temp_son = temp_son // 10  # sonni oxirgi raqamini ochirib tashlaymiz.

# farq = son - teskari_son
# print(farq)

# # 6-masala.

# son=int(input("Son kiriting: ")) # kiritilgan son.

# for i in range(1, son+1): # aylanish sikli  1dan songacha aylantirib beradi.
#     if son%i==0:  # shart son sikl beradigan songa qoldiqsiz bolinishini tekshiradi.
#         print(i, end=" ")  # agar qoldiqsiz bolinsa ekaranga i ni bosh joy bilan chiqaradi.

# # 7-masala.

# a=int(input("Boshlangich sonni kiriting: "))
# b=int(input("oxirgi sonni kiriting: "))

# for i in range(a, b+1):
#     if i%2!=0:
#         print(i)
#     else:
#         print(0-i)

# # 8-masala.

# son=int(input("son kiriting: ")) # kiritilgan son.
# count=0 # sanoqni sanash uchun.
# if son==0: # Agar son 0ga teng bolsa son 1ga teng
#     son=1
# else:  # Aks holda sonni almashtirib olamiz.
#     temp_son=abs(son)  # Agar kiritilgan son manfiy bolsa dastur xato qilmasligi uchun sonning modulini olamiz.
# while temp_son>0: # while siklida almashtirgan sonimiz 0dan kichik bolguncha aylantiramiz.
#     temp_son=temp_son//10 # Sonni har safar 10ga butun bolsak uning oxirgi raqami tushib qoladi.
#     count+=1  # Har bir raqam ochirilganda biz, bitta  xona sanaymiz.

# print(count, "xonali")  # kiritilgan son nechi xona ekanligini ekaranga chiqaramiz.



### Qiyin masalalar.

# # 1-masala. Fibonachiga doir masala.

# n=int(input("sonni kiriting: "))  
# a=0  
# b=1   # a = 0, b = 1: Ketma-ketlikni boshlab beruvchi asosiy sonlar.
# for i in range(n):  # Sikl n gacha aylanadi.
#     print(a, end=" ")    # print(a): Biz har doim a (birinchi turgan) sonni chiqaramiz.
    
#     temp=a+b   # Yangi son (temp) har doim a + b ga teng bo'ladi.
#     a=b
#     b=temp   # Keyingi qadamga o'tishda a ning o'rniga b ni, b ning o'rniga esa yangi chiqqan temp ni qo'yamiz.


