def letters_range(start, end, step=1):
    letrange = list()
    for one in range(ord(start), ord(end), step):
        letrange.append(chr(one))
    return letrange
