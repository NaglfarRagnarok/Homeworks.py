def common_elements():
    """
    Генерує множини чисел, кратних 3 і кратних 5,
    та повертає їхній перетин.
    :return: set[int] — множина спільних елементів
    """
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}
    return multiples_of_3 & multiples_of_5


# --- Тести ---
assert common_elements() == {0, 15, 30, 45, 60, 75, 90}, "Test failed"

print("ОК ✅")
