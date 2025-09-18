# ДЗ 6.3. Добуток чисел

def multiply_digits_until_single(n: int) -> int:
    """
    Перемножує всі цифри числа, доки результат не стане <= 9.
    :param n: початкове число
    :return: однозначний результат
    """
    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
    return n


if __name__ == "__main__":
    number = int(input("Введіть ціле число: "))
    result = multiply_digits_until_single(number)
    print(result)