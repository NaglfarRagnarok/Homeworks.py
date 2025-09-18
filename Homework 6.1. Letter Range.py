import string

# вхідні дані
s = input("Введіть діапазон (наприклад a-c): ")

# розбиваємо на дві букви
start, end = s.split('-')

# беремо всі літери англійського алфавіту
letters = string.ascii_letters   # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# знаходимо індекси початку і кінця
i1 = letters.index(start)
i2 = letters.index(end)

# виводимо діапазон
print(letters[i1:i2+1])
