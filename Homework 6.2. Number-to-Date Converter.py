# ДЗ 6.2. Конвертер із числа в дату

def seconds_to_date(n: int) -> str:
    """
    Перетворює кількість секунд у формат: X день/дні/днів, ГГ:ХХ:СС.
    :param n: кількість секунд (0 <= n < 8 640 000)
    :return: відформатований рядок
    """
    seconds_in_minute = 60
    seconds_in_hour = 60 * seconds_in_minute
    seconds_in_day = 24 * seconds_in_hour

    days, remainder = divmod(n, seconds_in_day)
    hours, remainder = divmod(remainder, seconds_in_hour)
    minutes, seconds = divmod(remainder, seconds_in_minute)

    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    # правильне закінчення для "день"
    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    return f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}"


if __name__ == "__main__":
    n = int(input("Введіть кількість секунд (0 <= n < 8640000): "))
    print(seconds_to_date(n))
