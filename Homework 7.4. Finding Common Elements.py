"""
Скрипт для пошуку другого входження підрядка у тексті.
Написано відповідно до PEP 8.
"""


def second_index(text: str, substring: str) -> int | None:
    """
    Повертає індекс другого входження підрядка `substring` у рядку `text`.

    :param text: Рядок, у якому виконується пошук.
    :param substring: Підрядок, який потрібно знайти.
    :return: Індекс другого входження або None, якщо немає.
    """
    first = text.find(substring)
    if first == -1:
        return None

    second = text.find(substring, first + 1)
    if second == -1:
        return None

    return second


def main() -> None:
    """Проста перевірка функції second_index."""
    assert second_index("sims", "s") == 3, "Test1"
    assert second_index("find the river", "e") == 12, "Test2"
    assert second_index("hi", "h") is None, "Test3"
    assert second_index("Hello, hello", "lo") == 10, "Test4"
    print("Усі тести пройдено успішно ✅")


if __name__ == "__main__":
    main()
