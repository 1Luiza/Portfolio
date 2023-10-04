"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""
b_list = ['attribute', 'класс', 'функция', 'type']

for el in b_list:
    try:
        i = el.encode('ascii')
        print(f"{el} - можно записать в байтовом формате")
    except:
        print(f"{el}  - невозможно записать в байтовом формате")