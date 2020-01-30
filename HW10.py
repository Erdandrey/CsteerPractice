Counter = 0
print('Введи натуральное число.')
Number = int(input())
while Number != 1:
    if Number % 2:
        Number = Number*3 + 1
        Counter = Counter + 1
    else:
        Number = Number // 2
        Counter = Counter + 1
print('Число шагов для данного числа: ', Counter)
