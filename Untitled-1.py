import random
#t = int(input("Введите температуру воды"))
t = int (random.random()*200
if t < 0:
  print("Вода - замерзла")
if t >= 0 and t <= 100:
   print("Вода в жидком состоянии")
if t > 100:
    print("Вода в газообразном состоянии")