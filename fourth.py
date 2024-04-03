import csv
import main
"""
Функция fourth не принимает аргументов
fields, monsters - информация о названиях столбцов и монстрах, соответственно (с.м main)
dict - словарь вида {класс монстра: [количество монстров данного класса, суммарная сила атаки класса]
names - множество классов монстров
name = имя отдельно взятого монстра
value - список, т.е значение по ключу класса монстра
av - среднее значение силы атаки по классу
"""

def fourth():
    dict = {}
    names = set()
    fields, monsters = main.info()
    for x in monsters:
        names.add(x[0].split()[1])
    for i in names:
        dict[i] = [0, 0]
    for j in monsters:
        name = j[0].split()[1]
        value = dict[name]
        value[0] += 1
        value[1] += int(j[3])


    for e in dict.keys():
        av = dict[e][1] / dict[e][0]
        print(f"Количество монстров класса {e} - {dict[e][0]}, среднее значение силы атаки по классу - {round(av, 3)}")
fourth()