n1, n2, n3 = map(int, input("Введите высоты трех башен: ").split())
max = n1
if n2 > max:
    max = n2
if n3 > max:
    max = n3
min = n1
if n2 < min:
    min = n2
if n3 < min:
    min = n3
middle = n1 + n2 + n3 - max - min
print(max, middle, min)