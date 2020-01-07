print("Введите целые неотрицательные числа,"
      "разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).:")
TextString = input()
Num = 0
Sum = 0
Flag = 1
for one in TextString:
    if one.isdigit():
        Num = Num*10 + int(one)
    elif one == '-':
        Num = Num * Flag
        Sum = Sum + Num
        Num = 0
        Flag = -1
    else:
        Num = Num*Flag
        Flag = 1
        Sum = Sum + Num
        Num = 0

if Num != 0:
    Num = Num * Flag
    Sum = Sum + Num
print(Sum)
