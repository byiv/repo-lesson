# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.


def my_sum_func(arg):
    res = 0
    for i in range(len(arg)):
        res += int(arg[i])
    return res


def my_func_split_sum(my_string_arg):
    my_list = my_string_arg.split()
    return my_sum_func(my_list)


my_sum = 0
while True:
    my_string = input('Введите числа разделенные пробелом: ')
    if my_string.endswith('!'):
        my_string = my_string.replace('!', '')
        my_sum += my_func_split_sum(my_string)
        print(my_sum)
        break
    my_sum += my_func_split_sum(my_string)
    print(my_sum)
