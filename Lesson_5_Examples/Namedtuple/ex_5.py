"""Класс collections.namedtuple()"""

from collections import namedtuple

# 'Resume' - имя кортежа
RES = namedtuple('Resume', 'id first_name second_name')
RESUME_PARTS = RES(
    id='1',
    first_name='Ivan',
    second_name='Ivanov'
)

print(RESUME_PARTS)
print(RESUME_PARTS.id)

# Resume(id='1', first_name='Ivan', second_name='Ivanov')
# 1