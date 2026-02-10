# 15-dars. Lug'at elementlari bilan ishlash
# 8/02/2026
# Muallif: Otabek

# talaba_0 = {
#     'ism':'otabek',
#     'familiya':'shodiev',
#     'yosh':'22',
#     'fakultet':'matematika',
#     'kurs':'1',
#     'daraja':'magistr'}
# # .items() metodi lug'at ichidagi barcha juftliklarni chiqaradi
# print(talaba_0.items())
# # agar for sikli bilan chaqirsak tushunarliroq chiqaradi
# for k,q in talaba_0.items():
#     print(f"Kalit: {k}")
#     print(f"Qiymat: {q}\n")

# .keys() metodi faqat kalitlarni chiqaradi

# mahsulotlar = {
#      'olma': 5000,
#      'nok':7000,
#      'anor':10000,
#      'kivi':20000}
# print(mahsulotlar.keys())
# print("Do'kondagi mahsulotlar")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
# tartiblangan ko'rinishda chiqaradi

# bozorlik = ['anor','uzum','olma','banan']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos,{buyum} ham olib keling")
# # Lug'at elementlarini tartib bilan chiqarish
# print("Do'kondagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# .values() metodi

# print(mahsulotlar.values())
# for m in mahsulotlar.values():
#     print(m)

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)
# # qiymatlar necha marta bo'lsa shuncha marta chiqaradi

# # .set() funksiyasi

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)

   