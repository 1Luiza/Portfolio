"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def division(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return "введите число больше 0"


a = int(input("Введите а: "))
b = int(input("Введите b: "))
print(division(a, b))
