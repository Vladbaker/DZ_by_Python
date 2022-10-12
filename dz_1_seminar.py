# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day_numbers = int(input('Введите номер дня недели '))
# if day_numbers < 1 or day_numbers > 7:
#     print('Ошибка')
# if day_numbers == 6 or day_numbers == 7:
#     print('Выходной день')
# if day_numbers == 1 or day_numbers == 2 or day_numbers == 3 or day_numbers == 4 or day_numbers == 5:
#     print('Будний день')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

X = int(input('Введите координату X '))
Y = int(input('Введите координату Y '))

if X == 0 and Y == 0:
    print('Ошибка')
if X > 0 and Y > 0:
    print('1')
if X > 0 and Y < 0:
    print('4')
if X < 0 and Y < 0:
    print('3')
if X < 0 and Y > 0:
    print('2')