def pow_num(x):
    """
    Обчислює квадрат числа.

    Параметри:
        x (int | float): вхідне число.

    Повертає:
        int | float: квадрат числа.
    """
    return x ** 2


def some_gen(begin, count, func):
    """
    Генераторна функція, яка формує послідовність чисел.

    Параметри:
        begin (int | float): перший елемент послідовності.
        count (int): кількість елементів послідовності (включаючи перший).
        func (callable): функція, яка визначає правило утворення наступного елемента.

    Yield:
        int | float: наступний елемент послідовності.
    """
    value = begin
    for _ in range(count):
        yield value
        value = func(value)


def main():
    """
    Тестування роботи генератора.
    """
    from inspect import isgenerator

    gen = some_gen(2, 4, pow_num)

    assert isgenerator(gen) is True, 'Test1'
    assert list(gen) == [2, 4, 16, 256], 'Test2'
    print('OK')


if __name__ == "__main__":
    main()
