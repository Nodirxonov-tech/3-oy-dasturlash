print("Fayl yuklanish vaqtini hisoblash.")
fayl_hajmi = int(input("Fayl hajmini (Mb) da kiriting: "))
internet_tezlik = int(input("internet tezligini kiriting: (Mb/s)"))
vaqt = (fayl_hajmi * 8) / internet_tezlik
print("fayl", vaqt, "soniyada yuklanadi.")
