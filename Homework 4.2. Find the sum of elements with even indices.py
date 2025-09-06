def sum_even_indices(lst):
    # Беремо елементи з парними індексами (0, 2, 4, …) і рахуємо суму
    return sum(lst[::2]) if lst else 0


# 🔹 Перевірка на прикладах
print(sum_even_indices([1, 2, 3, 4, 5, 6]))   # 9  (1 + 3 + 5)
print(sum_even_indices([10, 20, 30]))         # 40 (10 + 30)
print(sum_even_indices([7]))                  # 7
print(sum_even_indices([]))                   # 0
