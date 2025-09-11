import string
import keyword

name = input("Введіть ім'я змінної: ")

# 1. Порожній рядок
if not name:
    print(False)

# 2. Починається з цифри
elif name[0].isdigit():
    print(False)

# 3. Більше ніж одне підкреслення поспіль
elif "__" in name:
    print(False)

# 4. Містить великі літери
elif any(ch.isupper() for ch in name):
    print(False)

# 5. Містить пробіли або заборонені символи (пунктуація без "_")
elif any(ch in string.punctuation.replace("_", "") or ch.isspace() for ch in name):
    print(False)

# 6. Є зареєстрованим словом Python
elif name in keyword.kwlist:
    print(False)

# ✅ Якщо всі перевірки пройдено
else:
    print(True)
