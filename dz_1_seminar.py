day_numbers = int(input('Введите номер дня недели '))
if day_numbers < 1 or day_numbers > 7:
    print('Ошибка')
if day_numbers == 6 or day_numbers == 7:
    print('Выходной день')
if day_numbers == 1 or day_numbers == 2 or day_numbers == 3 or day_numbers == 4 or day_numbers == 5:
    print('Будний день')