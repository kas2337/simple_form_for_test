
ru_RU = {
    "а": 1,
    "б": 2,
    "в": 3,
    "г": 4,
    "д": 5,
    "е": 6,
    "ё": 7,
    "ж": 8,
    "з": 9,
    "и": 10,
    "й": 11,
    "к": 12,
    "л": 14,
    "м": 13,
    "н": 15,
    "о": 16,
    "п": 17,
    "р": 18,
    "с": 19,
    "т": 20,
    "у": 21,
    "ф": 22,
    "х": 23,
    "ц": 24,
    "ч": 25,
    "ш": 26,
    "щ": 27,
    "ъ": 28,
    "ы": 29,
    "ь": 30,
    "э": 31,
    "ю": 32,
    "я": 33,
}

def is_substr_in_alphabet(input_str: str) -> bool:
    for substr in input_str:
        if substr in ru_RU.keys():
            return True
    return False

def get_letter_number(letter: str) -> int:
    number = ru_RU.get(letter.lower(), 0)
    return number
