n1, n2, n3 = map(int, input("Введите колличество подданных: ").split())
if n1 == n2 == n3:
    print(3)
elif n1 == n2 or n1 == n3 or n2 == n3:
    print(2)
else:
    print(0)