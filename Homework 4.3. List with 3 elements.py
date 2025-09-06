import random

# створюємо список випадкової довжини від 3 до 10
lst = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
print("Original list:", lst)

# формуємо новий список [перший, третій, другий з кінця]
new_lst = [lst[0], lst[2], lst[-2]]
print("New list:", new_lst)
