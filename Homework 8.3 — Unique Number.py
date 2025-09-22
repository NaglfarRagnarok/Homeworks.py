def find_unique_value(some_list):
    """
    Знаходить і повертає унікальне число зі списку.

    :param some_list: list[float|int] — список чисел
    :return: float|int — число, яке зустрічається лише один раз
    """
    for value in some_list:
        if some_list.count(value) == 1:
            return value


# --- Тести ---
assert find_unique_value([1, 2, 1, 1]) == 2, "Test1"
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, "Test2"
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, "Test3"

print("ОК ✅")
