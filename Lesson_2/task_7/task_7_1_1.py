# Второй вариант

def cycle_method(num):
	m = 0
	s = 0
	for i in range(1, num + 1):
		s += i
		m = num * (num + 1) // 2
	print(f'Равенство {s == m}')


try:
	NUMB = int(input("Введите число: "))
	cycle_method(NUMB)
except ValueError:
	print('Ошибка, нужно ввести целое число!')