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
    dict_sim = {}

    with open(file_name) as f:
        for n in f.readlines():
            for simv in n:
                if simv in dict_sim:
                    dict_sim[simv] += 1
                else:
                    dict_sim[simv] = 1

    return dict_sim


def pig_it(text: str):
    result_list = []
    punctuation_list = ["!", ".", ",", "?", ":", ";"]
    words_list = text.split()
    for word in words_list:
        if word in punctuation_list:
            result_list.append(word)
        else:
            result_list.append(word[1:] + word[0] + 'ay')
    result = ' '.join(result_list)
    return result


def create_phone_number(n: list):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)


def snail(ar: list):
    result = []
    result.extend(ar[0])
    ar.pop(0)
    if len(ar) > 0:
        for x in range(0, len(ar)):
            result.append(ar[x][-1])
            ar[x].pop(-1)
        for x in range(len(ar[-1]) - 1, -1, -1):
            result.append(ar[-1][x])
        ar.pop(-1)
        for x in range(len(ar) - 1, -1, -1):
            result.append(ar[x][0])
            ar[x].pop(0)
        if ar:
            result.extend(snail(ar))
    return result


def snail_best(array: list):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a


def one(operation=None): return operation(1) if operation else 1


def two(operation=None): return operation(2) if operation else 2


def plus(number: int): return lambda x: x + number



if __name__ == '__main__':
    print("Это библиотека, а не исполняемый файл.")
