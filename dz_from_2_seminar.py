Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


number = input('Введите число: ')

summa = 0
for i in number:
    if i.isdigit():
        summa +=int(i)
print(summa)

Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('Введите число: '))

composition = 1
for i in range(N):
   i+=1
   composition*=i
   print(composition, end=' ')

Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input())
lst = [round((1+1/n)**n) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst))}')
