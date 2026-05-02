# # 1-masala
# celsiya=float(input("selsiy haroratni kiriting: "))
# farangeyt=celsiya*1.8+32
# status = ["sovuq", "iliq"][celsiya > 20]
# print(f"{celsiya}°C = {farangeyt}°F — bu {status} kun!")

# # 2-masala.
# yil=int(input("Tugilgan yilingizni yozing: "))
# print("Siz", 2026-yil, "yoshdasiz")

# # 3-masala.
# soat=int(input("soatni kiriting: "))
# print(soat, "soat =", soat*3600, "soniya")

# # 4-masala.
# son=str(input("son kiriting: "))
# print(son [::-1])

# # 5-masala.
# matn=(input("3ta harf kiriting: "))
# kod1= ord(matn[0])
# kod2= ord(matn[1])
# kod3= ord(matn[2])
# yigindi=kod1+kod2+kod3
# print(f"Sizning yangi parolingiz: {matn}{yigindi}")

# # 6-masala.
# soat=int(input("Soatni kiriting: "))
# daqiqa=int(input("Daqiqani kiriting: "))
# print("Film davomiyligi: ",(soat*60)+daqiqa, "daqiqa")

# # 7-masala.
# matn=str(input("Matn kiriting: "))
# print(matn.upper() [::-1])


# # 8-masala.
# id_raqam=(input("Raqamni kiriting: "))
# yil=id_raqam[:2]
# tugilgan_yil=int(yil)+2000
# yosh=2025-tugilgan_yil
# print("Yosh: ", yosh)


# # 9-masala.
# a=input("belgi kiriting: ")
# b=input("belgi kiriting: ")
# print(a+b)


# # 10-masala.
# soz1=input("1-sozni kiriting: ")
# soz2=input("2-sozni kiriting: ")
# soz=soz1+soz2
# uzunlik=len(soz)
# print(soz, (uzunlik))
# # print(soz1+soz2, len(soz1+soz2))


# # 11-masala.
# a=input("1-belgini kiriting: ")
# b=input("2-belgini kiriting: ")
# c=input("3-belgini kiriting: ")
# a=ord(a)
# b=ord(b)
# c=ord(c)
# yigindi=(a+b+c)
# print("Kodlar yigindisi: ", yigindi)


# # 12-masala.
# harf=input("HArf kiriting: ")
# harf=ord(harf)+2
# print((chr(harf)))


# # 13-masala.
# import random
# harf=chr(random.randint(97,122))
# fharf=(input("Harf kiriting: "))
# print("Sizning harfingiz: ", fharf)
# print("kompyuter harfi: ", harf)


# # 14-masala.
# ism=input("Ismingizni kiriting: ")
# bosh_kodi=ord(ism[0])
# oxir_kodi=ord(ism[-1])
# uzunligi=len(ism)
# yigindi=bosh_kodi+oxir_kodi+uzunligi
# print("kod: ", bosh_kodi,"+",oxir_kodi,"+",uzunligi,"=",yigindi)

# # 15-masala.
# import random
# kraqm=(random.randint(100,999))
# fraqam=input("Raqam kiriting: ")
# print("Sizning soningiz: ", fraqam)
# print("Kompyuter soni: ", kraqm)

# # 16-masala.
# son=input("Uch xonali son kiriting: ")
# son1=int(son[0])
# son2=int(son[1])
# son3=int(son[2])
# yigindi=son1+son2+son3
# kopaytma=int(son1*son2*son3)
# print("Yigindisi: ", yigindi)
# print("Kopaytmasi: ", kopaytma)

# # 17-masala.
# son=input("Torxonali son kiriting: ")
# print(son [::-1])


# # 18-masala.
# son=input("Besh xonali raqam kiriting: ")
# print(son[2])

# # 19-masala.
# son=input("Sonni kiriting: ")
# teskari=son[1]+son[0]
# print(teskari)

# # 20-masala.
# son=input("sonni kiriting: ")
# print(son[0]*2+son[1]*2+son[2]*2+son[3]*2)
