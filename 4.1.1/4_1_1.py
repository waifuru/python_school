
def transliterate(func):
    russian_to_english_mapping = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'ye', 'ж': 'zh', 'з': 'z',
            'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
            'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

    def wrapped(*args, **kwargs):
        russian_text = str(func(*args, **kwargs))
        english_text = ""

        for symbol in russian_text:
            lower_case_symbol = symbol.lower()
            if lower_case_symbol not in russian_to_english_mapping.keys():
                english_text += symbol
            else:
                en_symbol = russian_to_english_mapping[lower_case_symbol]
                if symbol.isupper():
                    en_symbol = en_symbol.upper()
                english_text += en_symbol

        return english_text

    return wrapped


@transliterate
def get_russian_text():

    return "Привет, я русский текст в транслите!"


@transliterate
def get_kek(capacity, a, b):
    return "Кек на русском"


if __name__ == '__main__':
    print(get_russian_text())
    print(get_kek())

