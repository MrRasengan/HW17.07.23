# Сумма трёхзначного числа

n = input('Введите 3-х значное число: ')
res = 0
if len(n) == 3:
    for i in n:
        res += int(i)
    print(res)
else:
    print('Вы ввели не 3-х значное число')