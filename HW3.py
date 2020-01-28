TextString = ''
while TextString != '1':
    print("Введите текст, содержащий любые слова, слоги, числа или их комбинации,"
          " разделенные пробелом (для выхода введите 1):")
    TextString = input()
    TextString = TextString.lower()
    TextList = TextString.split(' ')
    TextDict = dict()
    for one in TextList:
        if TextDict.get(one) is None:
            TextDict.update({one: 1})
        else:
            TextDict[one] = TextDict[one] + 1
    flag = 0
    FinalDict = dict()
    for one in TextDict:
        if TextDict[one] > flag:
            FinalDict.clear()
            FinalDict.update({one: TextDict[one]})
            flag = TextDict[one]
        elif TextDict[one] == flag:
            FinalDict.update({one: TextDict[one]})
    for one in FinalDict:
        print(FinalDict[one], ' - ', one)
