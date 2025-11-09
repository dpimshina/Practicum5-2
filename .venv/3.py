n = int(input("Введите четырехзначное число: "))
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
reversed = d * 1000 + c * 100 + b * 10 + a
if n == reversed:
    print("настоящее")
else:
    print("кривое")