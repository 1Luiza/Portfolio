"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""


def salary():
    time = float(input("Выработка в часах: "))
    rate = float(input("Ставка в часах: "))
    bonus = float(input("Премия: "))
    salary = time * rate + bonus
    print(f"заработная плата сотрудника: {salary}")


salary()
