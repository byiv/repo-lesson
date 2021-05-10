# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить её на экран

numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
with open('less_5_5.txt', 'w+') as my_file:
    for el in numbers_list:
        print(el, file=my_file, end=' ')
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))
