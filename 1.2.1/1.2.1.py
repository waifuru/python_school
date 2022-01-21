def task_1_2_1():
    mas = []

    eid_prefix = "D:TUpdaterController::SetUniqueParam(429): eid: "
    f = open("logs.txt")
    for line in f.readlines()[::-1]:
        if line.startswith(eid_prefix, 9):
            mas.append(line)
            if len(mas) == 2:
                break
    f.close()

    print("Последние eid: " + mas[0])
    print("Предпоследние eid: " + mas[1])

    first_dict = get_dict_from_eid_string(mas[0][9:].replace(eid_prefix, ""))
    second_dict = get_dict_from_eid_string(mas[1][9:].replace(eid_prefix, ""))

    print(first_dict)
    print(second_dict)

    result = {}
    # сложение множеств на случай если в одном наборе есть ключ, которого нет в другом
    keys = set(first_dict.keys()) & set(second_dict.keys())
    for key in keys:
        value_1 = first_dict[key]
        value_2 = second_dict[key]
        if value_1 != value_2:
            result[key] = 'Из последнего: ' + value_1 + ", " + 'Из предпоследнего: ' + value_2
    return result


def get_dict_from_eid_string(eid):
    result_dict = {}
    pairs = eid.split(";")
    for pair in pairs:
        splitted_pair = pair.split(".")
        key = splitted_pair[0]
        value = splitted_pair[1]
        result_dict[key] = value
    return result_dict


if __name__ == '__main__':
    print(task_1_2_1())
