# 2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы:
def slice_eight(sl):
    return sl[:8]  # первые восемь символов


def row_center(ln):
    row_center_start = len(ln) // 2
    row_center_end = row_center_start + 4
    sl_four_center = (ln[row_center_start:row_center_end])
    return sl_four_center


def slice_index_three(ln):
    sit = (ln[3::3])  # символы с индексами кратными трем
    return sit
