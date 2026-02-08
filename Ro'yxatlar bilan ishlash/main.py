# 8-dars. Ro'yxatlar bilan ishlash
# 4/02/2026
# Muallif: Otabek

# Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab qilinishi mumkin. Buning uchun list uchun maxsus .sort() metodidan foydalanamiz.
# .sort()

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#
# cars.sort() # bosh xarflar bo'lsa birinchi ular turadi ro'yxatda
# print(cars)

# cars = ['Bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# sorted()
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(sorted(cars)) # konsolga o'zgartiradi asosiysi o'z xolicha qoladi
# print(cars)

#sonlar = [3, 5, 7, 0,-65, -4.5, -1, 4.3]
# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True) # kattasidan kichiklashib tartiblaydi
# print(sonlar)

# Ro'yxatlarni aylantirish
# .reverse()

# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# fruits.reverse() # ro'yxat aylantiriladi
# print(fruits)
# print(len(fruits)) # len(fruits) ro'yxat uzunligini chiqaradi ya'ni elementlar soni

# range() funktsiyasi
# Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:

#sonlar = list(range(0,10)) # 0 dan 9 gacha bo'lgan sonlar ro'yxati chiqariladi range() shaklantiradi
# list()ro'yxat ko'rinishida saqlaydi
# range() ikkinchi indexdan bitta avval to'xtaydi
#print(sonlar)

# range () yordamida qadamniyam berish mumkin
# j_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# t_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", j_sonlar)
# print('Toq sonlar: ', t_sonlar)
# agar sonlar ketma ketligi 0 dan boshlansa faqat ikkinchi indexni yozsa xam bo'ladi misol uchun range(0,10) emas range(10) xato bo'lmaydi

# Sonli ro'yxat ustida sodda amallar
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
#sonlar = list(range(0,51))
# print(sonlar)
# print("Eng kichik son", min(sonlar))
# print("Eng katta son", max(sonlar))
# print("Sonlar yig'indisi ", sum(sonlar))

# ro'yxatni bir qismini kesib olish [1:5] ya'ni 1dan 4 gacha chiqaradi
# print(sonlar[0:11])
# sonlar0 = sonlar[0:6] # 0 chi dan 5 gacha kesib oladi
# print(sonlar0)

# Ro'yxatdan nusxa olish

# sonlar = [1, 2, 3, 4, 5]
# sonlar1 = sonlar # sonlar1 bilan sonlar ro'yxatini tenglaymiz
# sonlar1.append(7) # sonlar1 ga 7 ni qo'shamiz
# sonlar1.append(9) # sonlar1 ga 9 ni qo'shamiz
# # biz kutadigon natija sonlar1 da sonlar dagi elementlar va 7 bilan 9 qoshilishi kerak
# print('sonlar1:', sonlar1)
# print('sonlar:', sonlar)

# ikkalasi bir xil bo'lib qoldi demak nusxamiz o'xshamadi

# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar[:] # ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(7)
# sonlar2.append(9)
# print('sonlar: ', sonlar)
# print("sonlar2:",sonlar2)
 # bu xolatda faqat nusxamiz o'zgaradi

 # TUPLES - o'zgarmas ro'yxat

# tomonlar = (20, 30, 55.2)
# print(tomonlar)
# print(tomonlar[0])
# print(tomonlar[1])
# print(tomonlar[2])

# tomonlar[0] = 2
# print(tomonlar)
# xatolik o'zgartirib bo'lmaydi

# o'zgartirish uchun oddiy ro'yxatga aylantoriladi ya'ni (List)
# tomonlar = list(tomonlar) # type ni tekshirib ko'rish mumkin
# # endi o'zgartirsa bo'ladi
# tomonlar[0] = 2
# tomonlar.append(60)
# tomonlar = tuple(tomonlar)
# print(tomonlar)

# A M A L I Y O T

# davlatlar = ['Uzbekistan', 'Russia', 'Bangladesh', 'Amerika', 'Xitoy', 'Yaponiya']
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

j_sonlar = list(range(120,1201,2))
print(j_sonlar)
yigindi = sum(j_sonlar)

print("Sonlar yigindisi = ", yigindi)
kattasi = max(j_sonlar)
kichiki = min(j_sonlar)
ayirma = kattasi - kichiki
print("eng kattasi", kattasi)
print("eng kichiki", kichiki)
print("ayirmasi", ayirma)
print(len(j_sonlar))
b20 = j_sonlar[:21]
print(b20)
o20 = j_sonlar[-20:]
print(o20)
O = j_sonlar[530:550]
print(O)
