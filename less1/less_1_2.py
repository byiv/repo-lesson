second = int(input("Введите время в секундах: "))
print(f"HH:MM:SS {second//3600:02}:{second//60%60:02}:{second%60:02}")
