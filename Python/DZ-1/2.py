"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

import time

n = int(input("Введите время в секундах: "))
time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print(time_format)

# print(f"Время в формате ч:м:с - {secs / 3600:.2f} : {secs / 60:.2f} : {secs}")