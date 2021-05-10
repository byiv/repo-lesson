"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = list(input('Введите произвольную строку: '))
print(my_list)
position_num = 0
for el in range(len(my_list)//2):
    my_list[position_num], my_list[position_num + 1] = my_list[position_num + 1], my_list[position_num]
    position_num += 2
print(my_list)
