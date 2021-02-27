import random
# Открытие двери.
# Датчик движения.
# Температуры.
# Датчик света - возвращает освещенность.
# Счетчик пульса.
# Концентрация магнитного поля.
open = True
t = -14
t_list = [1,3,5,2,34,21,34,45,32]
print(t_list[5])
t_sum = sum(t_list)
print(t_sum)
n = len(t_list)
print(n)
avg = t_sum / n
print(avg)
t_list1 = []
for i in range(11):
    t_list1.append(int(random.random()*20))
print(t_list1)