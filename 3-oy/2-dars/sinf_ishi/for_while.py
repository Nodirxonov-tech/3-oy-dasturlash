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


# 1-masala.

n=int(input("son kiriting: "))
