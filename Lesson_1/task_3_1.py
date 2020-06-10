
try:
	X1_VAL = int(input('Введите значение координаты X1: \n'))
	Y1_VAL = int(input('Введите значение координаты Y1: \n'))
	X2_VAL = int(input('Введите значение координаты X2: \n'))
	Y2_VAL = int(input('Введите значение координаты Y2: \n'))
	try:
		K_ANG = (Y1_VAL - Y2_VAL) / (X1_VAL - X2_VAL)
		B_CONST = Y2_VAL - K_ANG * X2_VAL
		print(f'Уровнение прямой: y = {K_ANG}x + {B_CONST}')
	except ZeroDivisionError:
		print('Ошибка, деление на 0. Проверте корректность координат!')

except ValueError:
	print('Ошибка, нужно вводить целое число!')