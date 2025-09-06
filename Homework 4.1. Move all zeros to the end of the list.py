def move_zeros(lst):
    # Створюємо список без нулів
    non_zeros = [x for x in lst if x != 0]
    # Рахуємо кількість нулів
    zeros = [0] * (len(lst) - len(non_zeros))
    # Об’єднуємо
    return non_zeros + zeros


# 🔹 Перевірка на прикладах
print(move_zeros([0, 1, 0, 3, 12]))   # [1, 3, 12, 0, 0]
print(move_zeros([0, 0, 0]))          # [0, 0, 0]
print(move_zeros([1, 2, 3]))          # [1, 2, 3]
print(move_zeros([]))                 # []
