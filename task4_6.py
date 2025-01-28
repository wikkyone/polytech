def check_password(password):
    password_list = password.split("#")
    if (
        analyze_a(password_list[0])
        and analyze_b(password_list[1])
        and analyze_c(password_list[2]) == True
    ):
        print(f"Пароль {password} подходит под условия")
    else:
        print(f"Пароль {password} не подходит под условия")


def analyze_a(a):
    status_a = False
    if a == "00":
        status_a = False
    elif len(a) == 2:
        a = int(a)
        d = 2
        while a % d != 0:
            d += 1
        if a == d:
            status_a = True
    return status_a


def analyze_b(b):
    status_b = False
    if b == "000":
        status_b = False
    elif len(b) == 3:
        if b == b[::-1]:
            status_b = True
    return status_b


def analyze_c(c):
    status_c = False
    if c == "0":
        status_c = False
    elif len(c) == 1:
        c = int(c)
        if c % 2 == 0:
            status_c = True
    return status_c
