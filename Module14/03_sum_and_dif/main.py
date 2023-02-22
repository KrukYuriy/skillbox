def summ(N):
    summ = 0
    while N > 0:
        num = N % 10
        summ = summ + num
        N = N // 10
    print('Сумма чисел:', summ)
    return summ

def amount(N):
    count = 0
    while N > 0:
        count += 1
        N //= 10
    print('Количество цифр в числе:', count)
    return count

def difference(summ, count):
    difference = summ - count
    print('Разность суммы и количества цифр:', difference)

N = int(input('Введите число: '))

summ = summ(N)
count = amount(N)
difference(summ, count)