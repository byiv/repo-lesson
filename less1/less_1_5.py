proceeds = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издережек: "))
if proceeds > costs:
    print("Вы работаете с прибылью")
    profit = proceeds - costs
    print(f"Рентабильность выручки: {profit / proceeds * 100}%")
    employees_num = int(input("Введите численность сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {profit/employees_num}")
elif proceeds == costs:
    print("Вы работаете в 0")
else:
    print("Вы работаете в убыток")
