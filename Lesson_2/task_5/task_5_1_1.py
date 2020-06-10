first_ascii_num = 32
last_ascii_num = 127
STEP = 10


def ascii(from_sym, to_sym, output_str = ''):
    for i in range(from_sym, to_sym):
        if i <= last_ascii_num:
            output_str += f'{i} - {chr(i)} '     # Номер - символ
    return output_str

print("Это вывод цикла")
for i in range(first_ascii_num, last_ascii_num + 1, STEP):
    print(ascii(i, i + STEP))