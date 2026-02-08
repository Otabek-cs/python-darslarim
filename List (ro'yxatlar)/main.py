# 7-dars. List (Ro'yxatlar)
# 4/02/2026
# Muallif: Otabek

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narhlar = [12000, 18000, 20000,25000]
# sonlar = ['Bir', 'Ikki', 3, 4, 5]
# ismlar = []
# print(mevalar)
# print(narhlar)
# print(sonlar)
# print(ismlar)

#print("Birinchi meva: ", mevalar[0])
#mevalar [0] = 'anor'   # list da sanash 0 dan boshlanadi
#print(mevalar)
# .append
#mevalar.append("uzum")  # .append listni oxirida qo'shib qoyadi
#print(mevalar)

# .insert
#mevalar.insert(1, 'banan') # .insert qaysi o'rinda nima qo'shishligi uchun
#print(mevalar)

# cars = []
# cars.append('Lacetti')
# cars.append('Nexia')
# cars.append('Malibu')
# cars.append('tracker')
# print(cars)
# cars.insert(1, 'Cobalt' )
# print(cars)
# cars.insert(2,'Damas')
# print(cars)

# indeks bo'yicha o'chirish del funksiyasi orqali
# del cars[3]
# print(cars)

# element qiymati bo'yicha o'chirish uchun .remove('element nomi'). faqat birinchi mos tushgan elementni o'chiradi agar bir necha marta takrorlangan bo'sa
# index bilmagan xolda qo'l keladi
# cars.remove('Damas')
# print(cars)

# bozorlik = ['un', "yog'", 'banan', 'ananas', 'olma']
# mahsulot = bozorlik.pop(1) # index o'rnida turgan elementni sug'urib oladi
# print(mahsulot)
# mahsulot = bozorlik.pop() # index yozilmasa oxirgi elementni oladi
#
# print(mahsulot)

# A M A L I Y O T
#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:

# ismlar = []
# ismlar.append('Marjona')
# ismlar.append('Dilnoza')
# ismlar.append('Dilnura')
# print(ismlar)
# print("Salom " + ismlar[0] + ' bugun darsga borasanmi ?')
# print("Yaxshimisan " + ismlar[1] + ' uyga vazifani qildingmi ? ')
# print(ismlar[2] + ',' + " qachon uyga kelasan ?" )

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
#
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# sonlar = [2, 44, 6, 3.4, -45, 0.5]
# print(sonlar)
# sonlar [0] = 13
# print(sonlar)
# p = sonlar[2] * sonlar[5]
# print(p)
# print(sonlar)

#
# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
#  t_shaxslar =['Amir Temur', 'Alisher Navoiy', 'Manguberdi']
# z_shaxslar =['Otabek Maxkamov', 'Saida Mirziyoyeva', 'Shavkat Mirziyoyev']
# tarix = t_shaxslar.pop(2)
# zamon = z_shaxslar.pop(0)
# print("Men tarixiy shaxslardan " + tarix + ' bilan,\nzamonaviy shaxslardan esa ' + zamon + ' bilan suhbat qilishni istar edim ')

# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
#
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
#
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
#
# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
friends = []
friends.append("Ulug'bek")
friends.append("Jamshid")
friends.append("Sanjar")
friends.append("Jaxon")
friends.append("Majid")
print(friends)
friends.remove('Sanjar')
friends.remove('Jaxon')
print(friends)
friends.append('Shaxzod')
friends.insert(0,'Otabek')
friends.insert(2, 'Samandar')
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
print(mehmonlar)

