def check_input(elements):
    """
    Находит самую длинную строку в массиве
    Возвращает строку и её индекс
    Args: 
        elements (list): входной массив данных

    Returns:
            int: индекс строки
            str: самая длинная строка
    """
    max_len = 0
    index = -1
    max_string = ""

    for i, el in enumerate(elements):
        if isinstance(el, str):
            if len(el) > max_len:
                max_len = len(el)
                index = i
                max_string = el
    return index, max_string


def get_substring(s):
    """
    Находит самую длинную подстроку в строке
    Возвращает строку и её индекс

    Args: 
        s (str): исходная строка

    Returns:
            str: самая длинная подстрока
    """
    max_len = 0
    start = 0
    char_index = {}

    for i in range(len(s)):
        if s[i] in char_index and char_index[s[i]] >= start:
            start = char_index[s[i]] + 1
        char_index[s[i]] = i
        current_len = i - start + 1
        if current_len > max_len:
            max_len = current_len
            max_start = start

    return s[max_start:max_start + max_len]


def main(elements):
    """
    Принимает на вход список, находит самую длинную строку списка
    Полученную строку передает на метод get_substring
    Печатает на экран (с помощью print) индекс самой длинной строки в массиве
    и найденную подстроку.

    Args: 
        elements (list): входной массив данных

    Returns:
        None
    """
    index, max_string = check_input(elements)
    if index == -1:
        print(-1, '')
    else:
        longest_substring = get_substring(max_string)
        print(index, longest_substring)