Sum = 0
for one in range(1, 1000000, 2):
    Reverse = str(one)[::-1]
    BinOne = bin(one)[2:]
    BinReverse = BinOne[::-1]
    if (str(one) == Reverse) and (BinOne == BinReverse):
        Sum = Sum + one
print(Sum)
