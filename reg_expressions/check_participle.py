import re


LETTERS="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
assert len(LETTERS), 33

def regex_is_deeprichastie(str_for_check):
    pattern=r"^[а-яё]{2,}((у|ю)чи|(а|я)|вая|в|ши)(сь)?$"
    return re.search(pattern, str_for_check, flags=re.IGNORECASE) is not None


functions=[regex_is_deeprichastie,]

test_strings=["Рассказывая",
            "стул",
            "пролетев",
            "231531515",
            "извлёкши",
            "_+bjhiu",
            "промчавшись",
            "умывшись"
            ]

for f in functions:
    print("\n", f)
    for ts in test_strings:
        print(ts, regex_is_deeprichastie(ts))           