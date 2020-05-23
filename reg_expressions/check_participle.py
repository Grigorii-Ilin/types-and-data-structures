import re


LETTERS="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
LETTERS+=LETTERS.lower()
assert len(LETTERS), 33*2

def regex_is_prichastie(str_for_check):
    patter=r"^[А-Яа-яЁё]"