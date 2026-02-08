# 5-dars. String (matn)
# 3.02.2026
# Muallif: Otabek

#ism = 'Otabek'
#shahar = 'Buxoro'
#viloyat = 'Buxoro'
#smayl = '❤'
#print(smayl)

# String ustida amalar
#ism = 'Otabek'
#familiya = 'Shodiev'
#print(ism + ' ' + familiya)

# f-string
# ism = 'Otabek'
# familiya = 'Shodiev'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# ism = 'Dilnura'
# familiya = 'Shodieva'
# print(f"Salom, mening ismim {ism}. {ism} {familiya}!")

# Maxsus belgilar

# print("Buxoro shahar")
# print("Buxoro \tshahar") #\t probel kuproq tashaydi
# print("Buxoro \nshahar") # \n ikkinchi satrga tushiradi

# STRING METODLARI
# ism = "Otabek"
# familiya = "Shodiev"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper()) # upper() metodi xamma xarflarni katta qiladi

# ism = "otabek"
# familiya = "shodiev "
# ism_sharif = f"{ism} {familiya}"
# #print(ism_sharif.lower()) # lower () metodi xamma xarflarni kichikga yozadi
# #print(ism_sharif.title()) # title() metodi xamma birinchi xarflarni
# print(ism_sharif.capitalize()) # capitalize() metodi faqat birinchi so'zni birinchi xarfini katta qiladi

# meva = "    olma    "
# print(meva)
# print("Men " + meva.lstrip() + " yaxshi ko'raman") # lstrip() metodi matndan chapdagi(left) probelni oladi
# print("Men " + meva.rstrip() + " yaxshi ko'raman") # rstrip() metodi matndan o'ngdagi probelni oladi
# print("Men " + meva.strip() + " yaxshi ko'raman") # strip() ikkala tomondagi probellarni oladi

# INPUT funksiyasi

# ism = input("Ismingiz nima ? ") # \n>>> ismni yangi qatordan yozadi
# print("Assalomu alaykum," + ism) # title() ismni bosh xarf bilan yozadi

# A M A L I Y O T
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(kocha + " ko'chasi, " + mahalla + " mahalasi, " + tuman + " tumani, " + viloyat + " viloyati " )

# surab chiqaradi
# kocha = input("kocha nomi ? \n>>>")
# mahalla = input("mahalla nomi ? \n>>>")
# tuman = input("tuman nomi ?\n>>>" )
# viloyat = input("viloyat nomi ?\n>>>")
# print(kocha + " kochasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati.")

# verguldan keyin yangi qatordan chiqadi
# kocha = input("kocha nomi ? \n>>>")
# mahalla = input("mahalla nomi ? \n>>>")
# tuman = input("tuman nomi ?\n>>>" )
# viloyat = input("viloyat nomi ?\n>>>")
# print(kocha + " kochasi,\n " + mahalla + " mahallasi,\n " + tuman + " tumani,\n " + viloyat + " viloyati.")

# f-string yordamida chiqarish

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
manzil = f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati. "
print(manzil)
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())