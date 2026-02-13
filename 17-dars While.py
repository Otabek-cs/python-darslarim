# 17-dars. While sikli
# 13.02.2026
# Muallif: Otabek

# ism = input("Ismingiz nima?")
# savol = f"Salom, {ism.title()}. yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr")
# height = float(height)

# while() toki 

# son = 1
# while son<=7: # toki son 5 dan kichhik yoki teng ekan ...
#     print(son,end=' ') # sonni konsolga chiqaradi
#     son+=1 # songa 1 ni qo'shamiz
#     #son = son + 1 # teng kuchli
# print("Dastur tugadi")

# # while and input 

# print("Kiritilgan sonning kvadratini qaytaruchi dastur. ")
# savol = " Istalgan son kiriting "
# savol += "(dasturni tugatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
        
# print("Dastur tugadi")


# break while

# print("Kiritilgan sonning kvadratini qaytaruchi dastur. ")
# savol = " Istalgan son kiriting "
# savol += "(dasturni tugatish uchun 'exit' deb yozing): "
# while True: # abadiy sikl
#       qiymat = input(savol)
#       if qiymat=='exit':
#           break # siklni to'xtatadi
#       else:
#           print(float(qiymat)**2)
# print("Dastur tugadi")

# break for

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son ==8:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# Continue while for
# sonlar = list(range(1,11))
# for son in sonlar:
      #  if son ==8:
      #      continue
      # print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<=10:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
# print("Marxamat 10 gacha bo'lgan juft sonlar ro'xati")

# A M A L I Y O T


# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!')  
        
        