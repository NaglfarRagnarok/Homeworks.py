import string

MAX_LENGTH = 140


def make_hashtag(text: str) -> str:
    """
    Перетворює рядок у хештег за правилами:
    - видаляє символи пунктуації (string.punctuation);
    - кожне слово починається з великої літери;
    - хештег починається з '#';
    - довжина результату не перевищує 140 символів.
    """
    # Видалити пунктуацію
    clean = "".join(ch for ch in text if ch not in string.punctuation)

    # Розбити на слова і зробити перші літери великими
    words = clean.split()
    capitalized = [word.capitalize() for word in words]

    # Побудувати хештег
    hashtag = "#" + "".join(capitalized)

    # Обрізати до максимальної довжини
    return hashtag[:MAX_LENGTH]


if __name__ == "__main__":
    # Запитати рядок у користувача
    user_text = input("Введіть рядок для перетворення у хештег: ")
    result = make_hashtag(user_text)
    print("Результат:", result)

