def first_word(text: str) -> str:
    """Пошук першого слова в рядку."""
    # Замінюємо крапки та коми на пробіли
    cleaned = text.replace('.', ' ').replace(',', ' ')
    # Ділимо по пробілах і забираємо перше непорожнє слово
    for word in cleaned.split():
        if word:  # ігноруємо пусті елементи
            return word
    return ""  # якщо рядок порожній


# Тести
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print("OK")

