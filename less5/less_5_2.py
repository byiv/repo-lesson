# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('less_5_2.txt', 'r') as my_file:
    content = my_file.readlines()

words_count = 0
new_content = []
for el in range(len(content)):
    new_content = content[el].split()
    words_count += len(new_content)
strings_count = len(content)
print(f'Колличество строк в файле: {strings_count}')
print(f'Колличество слов в файле: {words_count}')

# Почему при таком варианте выдает ошибку?
# Unexpected type(s):(int, list[str])Possible type(s):(_SupportsIndex, str)(slice, Iterable[str])
#
# for el in range(len(content)):
#     content[el] = content[el].split()
#     words_count += len(content[el])
