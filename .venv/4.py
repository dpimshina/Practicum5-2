n = int(input("Введите натуральное число не превышающее 100: "))
a = n % 10
if 11 <= n <= 14:
    print(f"{n} попугаев")
else:
    if a == 1:
        print(f" {n} попугай")
    elif 2 <= a <= 4:
        print(f" {n} попугая")
    else:
        print(f" {n} попугаев")