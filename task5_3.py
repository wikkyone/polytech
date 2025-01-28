import time


def timer(stdin):
    time.sleep(int(stdin))
    return f"Время истекло! {stdin} секунд прошло."
