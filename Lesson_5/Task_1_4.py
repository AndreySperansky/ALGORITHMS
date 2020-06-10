from collections import defaultdict

COUNT_ORG = int(input('Введите количество предприятий для расчета прибыли: '))
COUNTER = COUNT_ORG
ORGANISATION = defaultdict(list)

while COUNTER > 0:
    NAME_ORG = input('Введите название предприятия: ')
    PROFIT_ORG = input('через пробел введите прибыль данного '
                       'предприятия за каждый квартал(Всего 4 квартала): ').split(' ')

    for el in PROFIT_ORG:
        ORGANISATION[NAME_ORG].append(int(el))
    COUNTER -= 1

NAMES_ORG = list(ORGANISATION.keys())
SUM_OF_ORG = 0
for el in NAMES_ORG:
    ORGANISATION[el] = sum(ORGANISATION[el])
    SUM_OF_ORG += ORGANISATION[el]
AVG_PROFIT = SUM_OF_ORG / COUNT_ORG

MAX_PROFIT = [el[0] for el in ORGANISATION.items() if AVG_PROFIT < el[1]]
MIN_PROFIT = [el[0] for el in ORGANISATION.items() if AVG_PROFIT > el[1]]
print(f'Средняя годовая прибыль всех предприятий: {AVG_PROFIT}')
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(MAX_PROFIT)}')
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(MIN_PROFIT)}')