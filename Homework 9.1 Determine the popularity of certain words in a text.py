def popular_words(text, words):
    """
    Повертає словник з кількістю входжень шуканих слів у тексті.

    Аргументи:
        text (str): рядок з текстом, у якому ведеться пошук
        words (list): список слів (у нижньому регістрі),
                      популярність яких потрібно визначити

    Повертає:
        dict: словник {слово: кількість входжень}
    """
    # Переводимо весь текст у нижній регістр
    lowered_text = text.lower().split()

    # Формуємо словник: для кожного слова з words рахуємо кількість у тексті
    result = {word: lowered_text.count(word) for word in words}

    return result


# ======= Тести =======
if __name__ == "__main__":
    assert popular_words(
        '''When I was One I had just begun When I was Two I was nearly new ''',
        ['i', 'was', 'three', 'near']
    ) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

    print("OK")