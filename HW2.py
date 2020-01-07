print("Введите текст, содержащий любые слова, слоги, числа или их комбинации,"
      " разделенные пробелом:")
TextString = input()
TextList = TextString.split(' ')
TextSet = set(TextList)
TextString = ' '.join(TextSet)
print(TextString)