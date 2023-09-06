# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”

def line_start(ln, first_word='Hello'):
    start_word = ln.startswith(first_word)
    if start_word:
        start_word = 'строка начинается с подстроки ' + first_word
    else:
        start_word = 'строка начинается с другого слова'
    return start_word


def line_end(ln, last_word='qwe'):
    end_word = ln.endswith(last_word)
    if end_word:
        end_word = 'строка заканчивается на: ' + last_word
    else:
        end_word = 'строка НЕ заканчивается на: ' + last_word
    return end_word
