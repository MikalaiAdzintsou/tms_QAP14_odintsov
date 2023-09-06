# Есть строка: test_string = "Hello world!", необходимо напечатать на каком месте находится буква w и кол-во l в строке

def w_place(ln):
    w = ln.find("w")
    w_number = w + 1
    return w_number


def l_count(ln):
    letter_l = ln.count('l')
    return letter_l
