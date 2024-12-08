from datetime import date, datetime
import random
import math
from decimal import Decimal


# ---------------------------------------------------------------

# 1 topshiriq

# class Harorat:
#
#     def sana_fun(self):
#         yil = random.randint(2000,2024)
#         oy = random.randint(1 , 12)
#         kun = random.randint(1 , 30)
#         sana = f"{yil}-{oy}-{kun}"
#         tasodifiy_sana = datetime.strptime(sana , "%Y-%m-%d")
#         return f"{tasodifiy_sana.strftime("%Y")}-{tasodifiy_sana.strftime("%m")}-{tasodifiy_sana.strftime("%d")}"
#
#
#     def tasodifiy_harorat_fun(self):
#         tasodifiy_gradus = Decimal(random.uniform(-10 , 40))
#         tasodifiy_gradus =  tasodifiy_gradus.quantize(Decimal('1.0'))
#         if tasodifiy_gradus < -50 or tasodifiy_gradus > 50 :
#             raise ValueError
#         return tasodifiy_gradus
#
#
#
# harorat1 = Harorat()
# print(f"Harorat: {harorat1.tasodifiy_harorat_fun()} °C Vaqt ({harorat1.sana_fun()})")
#


# ---------------------------------------------------------------

# 2 topshiriq


# class InsufficientFundsError(Exception):
#     def __init__(self ,massage):
#         self.massage = massage
#
#
#
# class Tekshirish:
#     def __set_name__(self, owner, name):
#         self.name ="_" + name
#
#     def __set__(self, instance, value):
#
#         if isinstance(value, (int, float, Decimal)):
#             value = int(value)
#             if value > 0:
#                 instance.__dict__[self.name] = value
#             else:
#                 try:
#                     raise InsufficientFundsError("Salbiy balansga tushib ketildi !!! ")
#                 except InsufficientFundsError as e:
#                     print(e.massage)
#         else:
#             return "Siz raqam orqali kirtmadingiz yechiladigon sumani"
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#
# class Tranzikatsiya:
#     suma = Tekshirish()
#     def __init__(self , suma):
#         self._suma = None
#         self.suma = suma
#         self.balans = 500000
#         self.sana_fun()
#
#
#     def sana_fun(self):
#         yil = random.randint(2000,2024)
#         oy = random.randint(1 , 12)
#         kun = random.randint(1 , 30)
#         sana = f"{yil}-{oy}-{kun}"
#         tasodifiy_sana = datetime.strptime(sana , "%Y-%m-%d")
#         return f"{tasodifiy_sana.strftime("%Y")}-{tasodifiy_sana.strftime("%m")}-{tasodifiy_sana.strftime("%d")}"
#
#     def pul_yechish(self):
#         if int(self.suma) < int(self.balans):
#             return f"Sana {self.sana_fun()}  . Hisobingiz {self.balans - self.suma} UZS pul qoldisizdan {self.suma} \n\033[32m{'Pul yechildi'} "
#
#         elif self.suma > self.balans:
#             return f"Sana {self.sana_fun()}  . Hisobingiz {self.balans} UZS pul bor {self.suma} yechishga uringanda xatolik \n\033[31m{'Xatolik: Balans yetarli emas!'}"
#
#
# hisob1 = Tranzikatsiya(Decimal("400000"))
# print(hisob1.pul_yechish())



# ---------------------------------------------------------------

# 3 topshiriq




# class Tekshirish:
#     def __set_name__(self, owner, name):
#         self.name ="_" + name
#
#     def __set__(self, instance, value):
#
#         if isinstance(value, (int, float, Decimal)):
#             if value > 0:
#                 instance.__dict__[self.name] = value
#             else:
#                 raise ValueError("Qiymat 0 dan katta bo'lishi kerak!")
#         else:
#             raise ValueError("Qiymat faqat raqam bo'lishi kerak!")
#
#
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#
#
#
#
# class Chipta:
#     narx = Tekshirish()
#     def __init__(self , narx):
#         self.narx = narx
#         self.sana = self.sana_fun()
#
#
#
#     def sana_fun(self):
#         yil = random.randint(2000,2024)
#         oy = random.randint(1 , 12)
#         kun = random.randint(1 , 30)
#         sana = f"{yil}-{oy}-{kun}"
#         tasodifiy_sana = datetime.strptime(sana , "%Y-%m-%d")
#         return f"{tasodifiy_sana.strftime('%Y')}-{tasodifiy_sana.strftime("%m")}-{tasodifiy_sana.strftime("%d")}"
#
#     def chipta(self):
#         return f"Chipta narxi: {self.narx}.000 UZS. Sotish sanasi {self.sana_fun()}"
#
# chiptaa1 = Chipta(Decimal("200"))
# print(chiptaa1.chipta())




# ---------------------------------------------------------------

# 4 topshiriq


#
# class Tekshirish:
#     def __set_name__(self, owner, name):
#         self.name ="_" + name
#
#     def __set__(self, instance, value):
#
#         if isinstance(value, (int, float, Decimal)):
#             if value > 0:
#                 instance.__dict__[self.name] = value
#             else:
#                 raise ValueError("Oylikni 0 dan katta bo'lishi kerak!")
#         else:
#             raise ValueError("Oylikni faqat raqam bo'lishi kerak!")
#
#
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#
#
#
#
# class Chipta:
#     narx = Tekshirish()
#     def __init__(self , narx):
#         self.narx = narx
#         self.sana = self.sana_fun()
#
#
#
#     def sana_fun(self):
#         yil = random.randint(2000,2024)
#         oy = random.randint(1 , 12)
#         kun = random.randint(1 , 30)
#         sana = f"{yil}-{oy}-{kun}"
#         tasodifiy_sana = datetime.strptime(sana , "%Y-%m-%d")
#         return f"{tasodifiy_sana.strftime('%Y')}-{tasodifiy_sana.strftime("%m")}-{tasodifiy_sana.strftime("%d")}"
#
#     def chipta(self):
#         return f"Oylik narxi: {self.narx}.000 UZS. Tolov sanasi {self.sana_fun()}"
#
# chiptaa1 = Chipta(Decimal("3000000"))
# print(chiptaa1.chipta())



















































