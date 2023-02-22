num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
def revers_number(number):
  x = int(number)
  n = 0
  while x > 0:
    digit = x % 10
    x = x // 10
    n = n * 10
    n = n + digit
  y = ''
  for i in reversed(str(number)):
    if i == '.':
      break
    y += i
  y = float('0.' + y)
  return n + y

print('\nПервое число наоборот: ',revers_number(num_1))
print('Второе число наоборот: ', revers_number(num_2))
print('Сумма: ', revers_number(num_1) + revers_number(num_2))

