n = int(input("Введите количество кнатов: "))
galleons = n // 493
d = n % 493
sickles = d // 29
knuts = d % 29
if galleons > 0:
    if galleons == 1:
        print("1 галлеон")
    else:
        print(f"{galleons} галлеонов")
if sickles > 0:
    if sickles == 1:
        print("1 сикль")
    else:
        print(f"{sickles} сиклей")
if knuts > 0:
    if knuts == 1:
        print("1 кнат")
    else:
        print(f"{knuts} кнатов")