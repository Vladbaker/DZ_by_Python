# N1 = int(input('Введите первое число '))
# N2 = int(input('Введите второе число '))

# if N2 == N1 * N1:
#     print('Да')
# elif N1 == N2 * N2:
#     print('Да')
# else:
#     print('Нет')

# max = int(input(f'Введите 1 число: '))

# for i in range(4):
#     i+=1
#     N = int(input(f'Введите {i+1} число: '))
#     if N > max:
#         max = N
# print(max)

N = int(input('Введите число N: '))
N = abs(N)

for i in range(-N, N+1):
    print(i, end=', ')