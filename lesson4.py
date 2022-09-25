# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# from math import pi
# d = int(input("Введите число для заданной точности числа Пи (сколько знаком после запятой показать):\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
# if num % i == 0:
# lst.append(i)
# num //= i
# i = 2
# else:
# i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# N = int(input())
# list = []
# for i in range(1,N+1):
# a = randint(-N,N+1)
# list.append(a)
# print(list)
# newlist = []
# for i in list:
# if i not in newlist:
# newlist.append(i)
# print(newlist)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random
# def write_file(st):
#     with open('file_004.txt', 'w') as data:
#         data.write(st)
# def rnd():
#     return random.randint(0,101)
# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))