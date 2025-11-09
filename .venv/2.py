import math
xc, yc, r, x, y = map(int, input("Введите данные: ").split())
if (xc - x) ^ 2 + (yc - y) ^ 2 > r ^ 2:
    print("Точка лежит вне окружности")
elif (xc - x) ^ 2 + (yc - y) ^ 2 < r ^ 2:
    print("Точка лежит внутри окружности")
else:
    print("Точка лежит на окружности ")