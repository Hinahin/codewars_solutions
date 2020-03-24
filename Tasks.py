def check_import():
    return "Импортировано успешно"


def second_task(code_text: str):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = ""

    for word in code_text:
        if word in abc:
            if abc.index(word) > 24:
                result += abc[1]
            elif abc.index(word) > 23:
                result += abc[0]
            else:
                result += abc[abc.index(word) + 2]
        else:
            result += word

    return result


if __name__ == '__main__':
    print("Привет мир!")
