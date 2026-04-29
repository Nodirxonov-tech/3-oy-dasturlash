# # 1-masala.
# a = 5
# if a:
#     print("true")
# else:
#     print("false")


# Oson masalalar.


# # 1-masala.

# son=int(input("Son kiriting: "))

# natija=(son%3==0)
# print(natija)

# # 2-masala

# son=int(input("Son kiriting: "))
# natija=(son%3==0) and (son%2 !=0)
# print(natija)


# # 3-masala.

# son = int(input("Son kiriting: "))  # Foydalanuvchi kiritadigan son.

# natija = (10 <= son <= 99)
# # Foydalanuvchi kiritgan son ikki xonaligini bilish sharti (son 10 dan katta yoki tengmi va son 99dan kichik yoki tengmi).
# print(natija)
# # Agar foydalanuvchi kiritgan son sharga mos bolsa (True) aks holda (False).


# # 4-masala.

# son = int(input("Son kiriting: "))  # Foydalanuvchi kiritadigan son.
# natija = (300 < son) and (son % 3 == 0)  # Foydalanuvchi kiritgan son 300dan katta va 3ga bolinadimini tekshirish.
# print(natija) # Natija son 300dan katta bolsa va 3ga bolinsa (True) aks holda (False) boladi.


# # 5-masala.

# son = int(input("Son kiriting: "))  # Kiritilgan son.

# natija = 15 <= son <= 20  # Son 15 dan katta yoki teng va son 20 dan kichik yoki teng.
# print(natija)  # Agar shart bajarilsa (True) aks holda (False) boladi.

# # 6-masala

# son = int(input("Son kiriting: "))  # kiritilxan 3xonali son.

# birinchi = son // 100  # Sonni boshidagi sonni matematik amal bilan ajratib olamiz.
# oxrgi = son % 10  # Oxirgi sonni olish.
# natija = (birinchi % 2 != 0) and (
#     oxrgi % 2 == 0
# )  # kiritilgan sonni boshini toqligini va oxirgi sonni juftligini aniqlash.
# print(natija)  # Agar shart qanoatlantirilsa (True) aks holda (False) boladi.


# # 7-masala

# son = int(input("Son kiriting: "))  # kiritilgan son.
# yuzlik = son // 100  # Birinchi sonni topish.
# onlik = (son // 10) % 10  # Ikkinchi sonni topish.
# birlik = son % 10  # Uchinchi sonni topish.
# yigindi = (yuzlik + onlik + birlik) - 1  # Ajratilgan sonlarni qoshish va 1 ni ayrib yigindini hisoblash.
# natija = yigindi % 2 != 0  # Chiqqan yigindi toq ekanligini aniqlash.
# print(natija)  # Shartni qanoatlantirsa (True) aks holda (False) boladi.


# # 8-masala.

# son=int(input("3 xonali son kiriting: "))
# yuzlik = son // 100  # Birinchi sonni topish.
# onlik = (son // 10) % 10  # Ikkinchi sonni topish.
# birlik = son % 10  # Uchinchi sonni topish.
# teskari=(birlik*100)+(onlik*10)+yuzlik  #Teskari sonni yasash.
# natija=100<=teskari<=999   # Teskari son 3 xonali ekanligini tekshiramiz
# print(natija)  # Shart qanoatlantirilsa (True) aks holda (False).


# Qiyin masalalar.


# # 1-masala.

# son1 = int(input("Son kiriting: "))  # 1-sonni kiritish.
# son2 = int(input("Son kiriting: "))  # 2-sonni kiritish.
# son3 = int(input("Son kiriting: "))  # 3-sonni kiritish.
# natija=son1<son2<son3    # sonni osish tartibida kiritilganligini tekshirish.
# print(natija)  # Agar shartni qanoatlantirsa (True) aks holda (False).


# # 2-masala.

# son1 = int(input("1-sonni kiriting: "))  # 1-soni kiritish.
# son2 = int(input("2-sonni kiriting: "))  # 2-soni kiritish.
# natija = (son1 % 2 != 0) and (son2 % 2 != 0)  # sonlarni ikkalasini toqligini tekshirish sharti.
# print(natija)  # Shartni qanoatlantirsa (True) aks holda (False) chiqadi.


# # 3-masala.

# a=int(input("1-sonni kiriting: "))   # 1-son.
# b = int(input("2-sonni kiriting: "))  # 2-son.
# natija=(a % 2 != 0 ) and (b % 2 == 0) or (a % 2 == 0) and (b % 2 != 0)  # ikki sondan kamida bittasi toq bolsa degan shart.
# print(natija)  # Shartni qanoatlantirsa (True) aks holda (False) chiqadi.


# # 4-masala.

# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# toq_a = a % 2 != 0  # a sonni toq ekanligini aniqlash.
# toq_b = b % 2 != 0  # b sonni toq ekanligini aniqlash.
# natija = toq_a != toq_b  # a va b son teng emas. Yani toq emas.
# print(natija)  # Shartni qanoatlantirsa (True) aks holda (False) chiqadi.


# # 5-masala.

# a=int(input("Son kiriting: "))
# b = int(input("Son kiriting: "))
# toq_b=(b%2!=0) # b ni toqligini tekshirish
# toq_a = a % 2 != 0  # a ni toqligini tekshirish
# juft_a = a % 2 == 0  # a ni juftligini tekshirish
# juft_b = b % 2 == 0  # b ni juftligini tekshirish
# natija=(toq_a==toq_b) or (juft_a==juft_b) #Shart agar a va b toq bolsa yoki juftmi?
# print(natija) # Shartni qanoatlantirsa (True) aks holda (False)

# #  6-masala

# a = int(input("Sonni kiriting: "))
# b = int(input("Sonni kiriting: "))
# c = int(input("Sonni kiriting: "))
# natija = (a) > 0 and (b) > 0 and (c) > 0  # shart a, b va c 0 dan kattami.
# print(natija)  # ha bolsa (True) aks holda (False). Agar qaysidir son manfiy bolsa shart qanoatlantirilmaydi.


# # 7-masala.

# a = int(input("Sonni kiriting: "))
# b = int(input("Sonni kiriting: "))
# c = int(input("Sonni kiriting: "))
# natija = (a > 0) or (b > 0) or (c > 0) # Shart agar bitta son musbat bolsa.
# print(natija)  # Agar bitta son musbat bolsa (True) aks holda (False)

# # 8-masala.

# son=int(input("son kiriting: "))
# natija=10<=son<=99  # Shart son q=10 dan katta yoki teng va son 99 dan kichik yoki tengmi
# print(natija) # shartni qanoatlantirsa (True) aks holda (False)

# # 9-masala.

# son=int(input("son kiriting: "))
# natija=(10<=son<=99)and(son%2==0)  # Shart son q=10 dan katta yoki teng va son 99 dan kichik yoki teng va kiritilgan son juft bolsa.
# print(natija) # shartni qanoatlantirsa (True) aks holda (False)

# # 10-masala.

# a = int(input("Birinchi son: "))
# b = int(input("Ikkinchi son: "))
# c = int(input("Uchinchi son: "))
# natija=(a==b)or(b==c)or(a==c)  # Shart hech bolmaganda uchta sondan 2 tasi tengmi.
# print(natija)  # Sharni qanoatlantirsa (True) aks holda (False).


## If masalalari.


# Oson.

# # 1-masala.

# son=int(input("Sonni kiriting: ")) # Foydalanuvchi kiritadigan son.
# if son%2==0:   # Shart son toqmi yoki juftmi
#     print("Juft")  # son juft bolsa bu chiqadi
# else:
#     print("Toq")   # son toq bolsa bu chiqadi.

# # 2-masala.

# kun=int(input("kunni kiriting: ")) # foydalanuvci kiritadigan kun (1,2...)
# if kun==1:  # Shart kiritilgan son 1 ga tengmi
#     print("Dushanba")
# elif kun==2:
#     print("Seshanba")
# elif kun == 3:
#     print("Chorshanba")
# elif kun == 4:
#     print("Payshanba")
# elif kun == 5:
#     print("Juma")
# elif kun == 6:
#     print("Shanba")
# elif kun == 7:
#     print("Yakshanba")
# else:
#     print("Bunday kun yoq")  # kiritilgan kun 7dan oshsa chiqadi.

# # 3-masala.

# ball=int(input("Ballni kiriting: "))
# if  80<=ball<=100:
#     print("5")
# elif 60<=ball<=79:
#     print("4")
# elif 40 <= ball <= 59:
#     print("3")
# elif 20 <= ball <= 39:
#     print("2")
# else:
#     print("1")


# # 4-masala.

# x=int(input("x ni kiriting: "))
# y = int(input("y ni kiriting: "))
# if x<0 and y>0:
#     print("II chorakda yotadi")
# elif x>0 and y>0:
#     print("I chorakda yotadi")
# elif x < 0 and y < 0:
#     print("III chorakda yotadi")
# elif x > 0 and y < 0:
#     print("IV chorakda yotadi")

# # 5-masala.

# son=int(input("son kiriting: "))
# if son%3==0 and son%5==0:
#     print("FizzBuzz")
# elif son%3==0:
#     print("Fizz")
# elif son % 5 == 0:
#     print("Buzz")


## Orta masalalar.

# # 1-masala.

# son=int(input("ikki xonali son kiriting: "))
# a=son//10
# b=son%10
# if a>b:
#     print(b)
# else:
#     print(a)

# # 2-masala.

# a = int(input("a burchakni kiriting: "))
# b = int(input("a burchakni kiriting: "))
# c = int(input("a burchakni kiriting: "))

# if a+b+c==180:
#     print("Bunday uchburchak mavjud")
# else:
#     print("Bunday uchburchak yoq")

# # 3-masala.

# belgi=input("belgi kiriting: ")
# unlilar="aeiouo'"
# if (
#     not belgi.isalpha()  # not — bu mantiqiy inkor operatori bo'lib, u (True) natijani False ga, (False) ni esa (True) ga aylantiradi.
# ):  # Birinchi navbatda .isalpha() orqali kiritilgan belgi harf ekanligini tekshiramiz. Agar harf bo'lsa, uni unlilar ro'yxatidan qidiramiz.
#     print("Bunday har yo'q")
# elif (
#     belgi in unlilar
# ):  # in operatori biror qiymat ma'lum bir to'plam (ro'yxat, satr, lug'at) ichida bor yoki yo'qligini tekshiradi.
#     print("Unli harf")
# else:
#     print("Undosh harf")

# # 4-masala.

# h1 = input("1-harfni kiriting: ")
# h2 = input("2-harfni kiriting: ")
# natija = h1.lower() == h2.lower()
# print(natija)


# 5-masala.

# harf = input("Harfni kiriting: ")
# n = int(input("n butun sonni kiriting: "))

# if not harf.isalpha():
#     print("Bunday harf yo'q")
# else:
#     start = (ord("A") if harf.isupper() else ord("a"))  # Harfning alifbodagi o'rnini aniqlaymiz (0-25 oraliqda)
#     yangi_o_rin = (ord(harf) - start + n) % 26  # Yangi harfning o'rnini hisoblaymiz (modul 26 alifbo aylanishi uchun)
#     print(chr(start + yangi_o_rin))  # Yangi harfni chiqaramiz

# # 6-masala.

# harf=input("Harf kiriting: ")
# natija=harf.upper()
# print(natija)


