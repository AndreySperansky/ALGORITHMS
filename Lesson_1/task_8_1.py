# Решение 2
def f1_year(YEAR):
	if YEAR % 400 or YEAR % 4 == 0 and YEAR % 400 == 0:
		print(f"Год {YEAR} - високосный")
	else:
		print(f"Год {YEAR} - невисокосный")


def f2_year(YEAR):
	if YEAR % 400 == 0 or YEAR % 4 == 0 and YEAR % 100 != 0:
		return print(f"Год {YEAR} - високосный")
	return print(f"Год {YEAR} - невисокосный")


try:
	Y = int(input("Введите год: "))
	f1_year(Y)
	f2_year(Y)

except:
	print("Вместо числа введена строка!")