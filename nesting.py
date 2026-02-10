# # 16-dars. Nesting (ya'ni lug'at ichida ro'yxatlar yoki aksincha)
# # 10.02.2026
# #Muallif: Otabek

# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avto'}

# car1 = {
#         'model':'Nexia',
#         'rang':'qora',
#         'yil': 2020,
#         'narh':8000,
#         'km':88000,
#         'korobka':'mexanika'}

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil': 2015,
#         'narh':13000,
#         'km':30000,
#         'korobka':'mexanika'}

# car = car0
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}-yil,{car['narh']} $")
          
# car = car1
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}-yil,{car['narh']} $")
# car = car2
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}-yil,{car['narh']} $")
                          
# # endi shuni qulayroq qilib chaqaramiz

# # cars = [car0, car1, car2]
# # for car in cars:
# #     print(f"{car['model'].title()},"
# #           f"{car['rang']} rang,"
# #           f"{car['yil']}-yil, {car['narh']} $")
    
# # # natija bir xil ln kodimiz yengilashti 
# # print(cars[0])
# # print(cars[0]['model'])      
# # print(f"{cars[2] ['rang'].title()} "
# #       f"{cars[2] ['model']}")

# malibus = [] # malibu mashinalari uchun bo'sh ro'yxat
# for n in range(10):
#     new_malibu = { # yar bir mashina uchun lug'at yaratamiz
                  
#         'model':'malibu',
#         'rang': None, # narhi noaniq
#         'yil': 2020,
#         'narh':None, # narhi noaniq
#         'km':0,
#         'korobka':'avto'}
#     malibus.append(new_malibu) #  yangi lug'atni ro'yxatga qo'shamiz

# for m in malibus[:3]:
#     m['rang'] = 'qizil'
# for m in malibus [3:6]:
#     m['rang'] = 'qora'
# for m in malibus [6:]:
#     m['rang'] = "ko'k"
#     m['korobka'] = 'mexanika'
    
# for m in malibus :
#     if m['korobka'] == 'avto':
#         m['narh'] = 40000
#     else:
#         m['narh'] = 35000
# for m in malibus:
#     print(malibus)

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())    

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
#     for til in tillar:
#         print(f'{til.upper()} ', end='')     

# A M A L I Y O T

# yusuf = {
#     'ism':'yusuf',
#     't_yil':2002,
#     't_joy':'buxoro',
#     'v_yil': 2000}

# qodiriy = {
#     'ism':'abdulla qodiriy',
#     't_yil': 1894,
#     'v_yil':1938,
#     't_joy':'toshkent'}

# navoiy = {
#     'ism':'alisher navoiy',
#     't_yil': 1441,
#     'v_yil': 1501,
#     't_joy':'xirot'
#     } 

# vohidov ={
#     'ism':'erkin vohidov',
#     't_yil': 1936,
#     'v_yil':2016,
#     't_joy':"farg'ona"}
# mashhurlar = [yusuf, qodiriy, navoiy,vohidov]
  
# for mashhur in mashhurlar:
#     ism = mashhur['ism']
#     t_yil = mashhur['t_yil']
#     v_yil = mashhur['v_yil']
#     t_joy = mashhur['t_joy']
#     print(f" {ism.title()} {t_yil} -yilda {t_joy.title()}da tavallud topgan.   "
#           f"{v_yil - t_yil} yil umr ko'rgan ")
    
davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    },
}

for davlat, info in davlatlar.items():
    if davlat.lower() == "aqsh":
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(
        f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
        f"\nHududi: {info['maydon']} kv.km"
        f"\nAholisi: {info['aholi']}"
        f"\nPul birligi: {info['pul birligi']}"
    )