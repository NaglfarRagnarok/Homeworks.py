
def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом (без урахування пунктуації та регістру).

    :param text: Вхідний рядок
    :return: True, якщо паліндром, інакше False
    """
    # Залишаємо тільки букви та цифри, переводимо до нижнього регістру
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

    # Порівнюємо з розвернутим рядком
    return cleaned == cleaned[::-1]


# --- Тести ---
assert is_palindrome("A man, a plan, a canal: Panama") is True, "Test1"
assert is_palindrome("0P") is False, "Test2"
assert is_palindrome("a.") is True, "Test3"
assert is_palindrome("aurora") is False, "Test4"

print("ОК ✅")
