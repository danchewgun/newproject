n = int(input("Ведите номер места от 1 до 54"))
if n % 2 == 0:
    s = "Верхнее"
else:
    s = "Нижнее"
if n in range(37, 55):
    s = s + " Боковое"
else:
    s = s + " Купе"
if n in range(1, 55):
    print("Ваше место -", s)
else:
    print("Неверное значение")
