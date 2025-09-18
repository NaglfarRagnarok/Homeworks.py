def read_number(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() == "q":
            raise SystemExit("Вихід з калькулятора.")
        try:
            return float(s)
        except ValueError:
            print("Помилка вводу! Введіть число або q для виходу.")

def read_operation():
    while True:
        op = input("Введіть дію (+, -, *, /): ").strip()
        if op in {"+", "-", "*", "/"}:
            return op
        print("Невідома дія! Дозволені: +, -, *, /")

print("Простий калькулятор. Натисніть q у полі числа, щоб вийти.")
while True:
    a = read_number("Введіть перше число: ")
    b = read_number("Введіть друге число: ")
    op = read_operation()

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    else:  # "/"
        if b == 0:
            print("Помилка! Ділення на нуль неможливе.")
            continue
        res = a / b

    print("Результат:", res)

    if input("Продовжити? (y/yes — так): ").strip().lower() not in ("y", "yes"):
        print("Калькулятор завершив роботу.")
        break
