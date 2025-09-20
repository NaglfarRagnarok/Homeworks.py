def second_index(text: str, some_str: str) -> int | None:
    """
    Повертає індекс другого входження підрядка `some_str`
    у рядку `text`. Якщо другого входження немає — повертає None.
    """
    first = text.find(some_str)  # шукаємо перше входження
    if first == -1:
        return None

    second = text.find(some_str, first + 1)  # шукаємо після першого входження
    if second == -1:
        return None

    return second


# --- Тести ---
assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"

print("ОК")
