import re

def regex_is_email(str_for_check:str):
    pattern=r"^[A-Za-z\d]+([.][A-Za-z-_\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,}$"
    return re.search(pattern, str_for_check) is not None


def sm_is_email(str_for_check:str):
    if len(str_for_check)<=6:
        return False

    LETTERS="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

    if str_for_check[0] not in LETTERS:
        return False

    if str_for_check.count("@")!=1:
        return False

    if str_for_check.count("..")>=1:
        return False

    at_parts=str_for_check.split("@")

    if at_parts[1].count(".")<=0:
        return False

    POSSIBLE_SYMBOLS=LETTERS+"0123456789_-"

    if str_for_check[-1] not in POSSIBLE_SYMBOLS:
        return False

    for at_part in at_parts:
        for dot_part in at_part.split("."):
            if dot_part[0] not in LETTERS:
                return False

            for s in dot_part[1:]:
                if s not in POSSIBLE_SYMBOLS:
                    return False

    return True
            

functions=[regex_is_email, sm_is_email]

test_strings=["asfd@mail.ru",
            ".hgvgyvg@bjh4jh.uh56h",
            "kjjk.lm09lk_lk.lkj@llj.oi45i-kj.sag",
            "bkjbnjn..kj@jhbjuh.cfm"
            ]

for f in functions:
    print("\n", f)
    for ts in test_strings:
        print(ts, regex_is_email(ts))




