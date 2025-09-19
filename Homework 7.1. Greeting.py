# ДЗ 7.1. Вітання

def say_hi(name: str, age: int) -> str:
    """
    Повертає вітальний рядок з ім'ям та віком людини.

    :param name: ім'я (рядок)
    :param age: вік (додатне ціле число)
    :return: вітальний рядок
    """
    return f"Hi. My name is {name} and I'm {age} years old"


if __name__ == "__main__":
    # Тести (перевірка роботи функції)
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
    print("ОК")

    # Додатково: ручне введення від користувача
    user_name = input("Введіть ім'я: ")
    user_age = int(input("Введіть вік: "))
    print(say_hi(user_name, user_age))



