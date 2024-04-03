import csv

"""
Функиця info является общей для предоставления данных из monster_game.csv
Общий массив monsters заполнен подмассивами с информацией о каждом монстре
Функция возвращает:
1. Масив fields и названиями столбцов
2. Массив monsters, состоящий из модмассивов с информацией о каждом монстре
"""

def info():
    with open('monster_game.csv', encoding='UTF-8') as csv_r:
        reader = csv.DictReader(csv_r, delimiter=',')
        fields = reader.fieldnames
        monsters = []
        for x in reader:
            monsters.append(list(x.values()))
        return fields, monsters
