n, k, m = map(int, input("Введите количество станций, номер ближайшей станции, номер необходимой станции: ").split())
if 1 <= k <= n and 1 <= m <= n:
    a = abs(k-m) - 1
    b = abs(k-m) - 1
    m = min(a, b)
    print(m)