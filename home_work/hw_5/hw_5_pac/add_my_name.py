#  Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.


def add_my_name(ln, my_name):
    spl_line = ln.split()
    spl_line[-1] = my_name
    new_line = ' '.join(spl_line)
    return new_line
