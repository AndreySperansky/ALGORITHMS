"""Одно из преимуществ использования namedtuple над обычным
кортежем заключается в том, что вам не нужно отслеживать
индекс каждого объекта, так как каждый объект назван
и доступен через свойство класса."""

from collections import namedtuple

Parts = namedtuple('Parts', 'id_num desc cost amount')
AUTO_PARTS = Parts(
    id_num='1234',
    desc='Ford Engine',
    cost=1200.00,
    amount=10
)

# выводим id: '1234'
print(AUTO_PARTS.id_num)

AUTO_PARTS = ('1234', 'Ford Engine', 12.00, 10)
# выводим цену: 12.00
print(AUTO_PARTS[2])

ID_NUM, DESC, COST, AMOUNT = AUTO_PARTS
# выводим id: '1234'
print(ID_NUM)
