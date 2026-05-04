# # 1-masala.

# n=int(input("Nechta raqam kiritasiz: "))  # Foydalanuvchi nechta son kiritishi.

# sonlar=[]   # Bu bizning savatimiz. kiritilgan sonlarni saqlash uchun.

# for i in range(n): # Tsikl aynan foydalanuvchi kiritgan n marta aylanishi uchun.

#     yangi_son=int(input(f"{i+1}-sonni kiriting: "))  # Har bir qadamda yangi son kiritish uchun.

#     sonlar.append(yangi_son)  # .append() bu metod Python royxatlariga yangi element qoshishning eng asosiy usulidir, u elementni doim royxatning oxiriga tirkab qoyadi.

# print(sonlar) # savatchamizga qoshilgan sonlarni chiqarish uchun printga sonlarni beramiz.


# # 2-masala.

# # Foydalanuvchi xoxlagancha son kiritishi uchun faqat orasi probel bilan.
# n=input("Sonni kiriting (probel bilan): ")
# # kiritilagan sonlarni ajratish uchun .split() ishlatiladi.
# sonlar=n.split()
# # Elementlar sonini topish uchun len() dan foydalanamiz.
# soni=len(sonlar)
# # kiritilgan elementlar oxirgisini topish uchun teskari tartibdan -1 indeksni olamiz.
# oxiri=sonlar[-1]
# # Teskari tartibda chiqarish uchun teskari indeksdan foydalanamiz.
# teskarisi=sonlar[::-1]
# # natijalarni ekranga chiqaramiz.
# print(f"Soni: {soni}\nOhirgisi: {oxiri}\nTeskarisi: {teskarisi}")


# # 3-masala.

# # Sonlarni probel bilan qabul qilib, royxatga aylantiramiz.
# sonlar=input("elementlarni probel orqali kiriting: ").split()
# # Qidirilayotgan sonni kiritamiz.
# qidiriladigan_son=input("qidiriladigan sonni kiriting: ")
# # 'in' operatiri yordamida royxatda borligini tekshiramiz. Yani qidirilayotgan son sonlar ichida bormi?
# if qidiriladigan_son in sonlar:
#     print("Ha, bor")
# else:
#     print("Bunday son yoq")


# # 4-masala.

# # sonlarni kiritamiz ba ularni butun songa (int) aylantiramiz.
# sonlar=[int(x) for x in input("sonlarni kiriting: ").split()]
# # slicing yordamida birinchi (0-indeks) va oxirgi (-1) elementlarni tashlav yuboramiz
# # [1: -1] = 1-indeksdan boshlab oxirigacha (oxirgi kirmaydi) degani.
# yangi_royxat=sonlar[1: -1]
# # Qolgan elementlarni tartiblaymiz,
# yangi_royxat.sort()
# # Natijani ekranga chiqaramiz.
# print(*(yangi_royxat))


