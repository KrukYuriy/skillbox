def min_divisor(num):
    if num%2 == 0:
      return 2
    i = 3
    while num%i != 0 and i*i <= num:
        i+= 2
    if i*i <= num: return i
    return num

number = int(input('Введите число: '))

print('Наименьший делитель, отличный от единицы:', min_divisor(number))