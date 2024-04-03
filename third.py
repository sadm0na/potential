import csv
import main

'''Функция third 
s - значение силы атаки
fields, monsters - информация о названиях столбцов и монстрах, соответственно (с.м main)
counter - количество монстров, которых возможно одолеть (монстров с 0 уровнем здоровьем убить нельзя)
Программа исполняется до введения слова 'хватит'
'''

def third():
    print('Введите значение силы атаки')
    s = input()
    counter = 0
    fields, monsters = main.info()
    while s != 'хватит':
        if s.isdigit():
            s = int(s)
            for x in monsters:
                if s > int(x[6]) and int(x[6]) != 0:
                    counter += 1
            if counter == 0:
                print("Вы очень слабы. Сходите и наберитесь опыта!")
            else:
                print(f"Вы сможете победить {counter} монстров")
        else:
            print('ведите положительное число')

        counter = 0
        s = input()
third()