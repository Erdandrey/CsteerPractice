while True:
    Num = 0
    Text = input()
    if Text == 'cancel':
        print('Bye!')
        break
    if Text.isdigit():
        if int(Text) % 2:
            Num = int(Text) * 3 + 1
        else:
            Num = int(Text) // 2
        print(Num)
    else:
        print('Не удалось преобразовать введенный текст в число.')
