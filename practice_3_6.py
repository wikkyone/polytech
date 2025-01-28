# запрашиваем логин и пароль
login = input()
password = input()
# проверяем наличие обоих условий сразу
if login == "student" and password == "0000":
    print("Вход разрешен!")
else:
    print("Ошибка. Вход запрещен")
