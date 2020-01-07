print("Введите текст, содержащий неотрицательные целые числа,"
      "разделенные через пробел:")
TextString = input()
TextList = TextString.split(' ')
NumberList = [int(one) for one in TextList]
NumberList.sort()
Range = 1
if NumberList[0] > 1:
    print(Range)
else:
    for one in NumberList:
        if (one - Range) <= 1:
            Range = one
        else:
            print(Range+1)
            Range = 0
            break
    if Range != 0:
        print(Range + 1)
