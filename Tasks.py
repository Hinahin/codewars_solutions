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


def third_task(file_name: str):
    dict_simv = {}

    with open(file_name) as f:
        for n in f.readlines():
            for simv in n:
                if simv in dict_simv:
                    dict_simv[simv] += 1
                else:
                    dict_simv[simv] = 1

    return dict_simv


if __name__ == '__main__':
    print("Привет мир!")
