import csv
import main

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
    writer.writerow({'opportunity': 'регенерация', 'power': maxx})
print(f'Максмальная мощность силы регенерации: {maxx}')