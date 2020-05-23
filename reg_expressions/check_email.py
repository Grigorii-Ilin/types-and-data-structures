import re

def regex_is_emai(s: str)->bool:
    pattern=r"^[A-Za-z\d]+([.][A-Za-z-_\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,}$"
    return re.search(pattern, s) is not None







