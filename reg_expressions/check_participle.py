import re


def regex_is_deeprichastie(str_for_check):
    pattern=r"^[а-яё]{2,}((у|ю)чи|(а|я)|вая|в|ши)(сь)?$"
    return re.search(pattern, str_for_check, flags=re.IGNORECASE) is not None


def sm_is_deeprichastie(str_for_check):
    if len(str_for_check)<=2:
        return False

    s_tmp=str_for_check

    if s_tmp[-2:]=="сь":
        s_tmp=s_tmp[:-2]

    suffixes=["учи", "ючи", "а", "я", "в", "ши"]
    for suffix in suffixes:
        suffix_len=len(suffix)
        if s_tmp[-suffix_len:]==suffix:
            s_tmp=s_tmp[:-suffix_len]
            break
    else:
        return False

    if len(s_tmp)<=1:
        return False

    LETTERS="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    LETTERS+=LETTERS.lower()
    assert len(LETTERS), 33*2

    for c in s_tmp:
        if c not in LETTERS:
            return False

    return True
    

functions=[regex_is_deeprichastie, sm_is_deeprichastie]

test_strings=["Рассказывая",
            "стул",
            "пролетев",
            "231531515",
            "извлёкши",
            "_+bjhiu",
            "промчавшись",
            "Умывшись",
            "ау"
            ]

for f in functions:
    print("\n", f)
    for ts in test_strings:
        print(ts, regex_is_deeprichastie(ts))           