first_year = int(input('Введите первый год: '))
second_years = int(input('Введите второй год: '))

print('\nГода от', first_year, 'до', second_years, 'тремя одинаковыми цифрами:')

for i in range(first_year, second_years + 1):
  a,b,c,d = i // 1000, i // 100 % 10, i // 10 % 10, i % 10
  if a == b == c or b == c == d or c == d == a or a == b == d:
    print(a * 1000 + b * 100 + c * 10 + d)