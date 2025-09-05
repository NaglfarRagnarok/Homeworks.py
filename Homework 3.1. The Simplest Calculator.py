# Homework 3.1. The Simplest Calculator

# Користувач вводить два числа
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# Користувач вводить дію
operation = input("Введіть дію (+, -, *, /): ")

# Виконуємо дію залежно від вибору
if operation == "+":
    result = a + b
    print("Результат:", result)
elif operation == "-":
    result = a - b
    print("Результат:", result)
elif operation == "*":
    result = a * b
    print("Результат:", result)
elif operation == "/":
    if b != 0:
        result = a / b
        print("Результат:", result)
    else:
        print("Помилка! Ділення на нуль неможливе.")
else:
    print("Невідома дія! Використовуйте тільки +, -, *, /")
