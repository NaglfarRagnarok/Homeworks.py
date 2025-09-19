# ДЗ 7.2. Модифікувати рядок

def correct_sentence(text: str) -> str:
    """
    Повертає виправлену копію речення так, щоб воно
    завжди починалося з великої літери та закінчувалося крапкою.

    :param text: вхідне речення (рядок)
    :return: виправлене речення
    """
    result = text[0].upper() + text[1:]
    if not result.endswith('.'):
        result += '.'
    return result


if __name__ == "__main__":
    # Тести
    assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
    assert correct_sentence("hello") == "Hello.", 'Test2'
    assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
    assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
    assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
    print("Тести пройдено успішно ✅")

    # Ввід користувача
    user_text = input("Введіть речення: ")
    fixed = correct_sentence(user_text)
    print("Виправлене речення:", fixed)

