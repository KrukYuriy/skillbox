print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
if x1 == x2:
    print('Уравнение вида y = k * x + b составить нельзя, т.к. x1 - x2 = 0, а на 0 делить нельзя')
else:
    k = y_diff / x_diff
    b = y2 - k * x2

    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)