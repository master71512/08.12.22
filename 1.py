# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

new_list = list(filter(lambda x: 9 < x < 100, map(int, input('введите список чисел через пробел:\n').split())))
print('Двузачные числа в списке:', *new_list)