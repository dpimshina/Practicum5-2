pin = input("Введите четырехзначный пароль: ")
if len(pin) != 4:
    print("ERROR")
else:
    num = int(pin)
    if len(set(pin)) != 4 or 1900 <= num <= 2050:
        print("ERROR")
    else:
        print("OK")