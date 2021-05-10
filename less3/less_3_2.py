# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Осуществить вывод данных
# о пользователе одной строкой.

def print_user_data(name, lastname, year_of_birth, city, email, phone):
    print(name, lastname, year_of_birth, city, email, phone)


print_user_data(lastname='Byzov', name='Ivan', year_of_birth=1985,
                city='Анапа', phone='89186400613', email='b.ivan.s85@gmail.com')
