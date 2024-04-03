import csv
import main

'''
fields, monsters - информация о названиях столбцов и монстрах, соответственно (с.м main)
maxx - максимально возможная мощность силы регенерации
percent - процент вероятности (выраженный в десятичной дроби)
krit - мощность силы регенерации у отдельно взятого монстра

В конце функции записываем нужные нам данные в файл monster_opportunity.csv
'''
def first():
    maxx = 0
    fields, monsters = main.info()
    for x in monsters:
        if x[1] == 'регенерация':
            percent = int(x[2]) * 0.01
            krit = int(x[5]) * percent
            maxx = max(maxx, krit)

    with open('monster_opportunity.csv', encoding='UTF-8') as wr:
        writer = csv.DictWriter(wr, fieldnames=['opportunity', 'power'])
        writer.writeheader()
        row = {'opportunity': 'регенерация', 'power': maxx}
        writer.writerow(row)
    print(f'Максмальная мощность силы регенерации: {maxx}')

first()
