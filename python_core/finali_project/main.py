from InquirerPy import prompt
import json
import requests

url_privat = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

res = requests.get(url_privat).json()

kurs = float(res[1]['sale'])


def get_input_text(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError(
                    "Поле не може бути порожнім. Будь ласка, введіть дані.")
            return user_input
        except ValueError as e:
            print(e)


def get_input_number(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError(
                    "Поле не може бути порожнім. Будь ласка, введіть дані.")
            user_input = user_input.strip()  # Видалення зайвих пробілів
            user_input = float(user_input)
            if user_input <= 0:
                raise ValueError("Введіть додатнє число.")
            return user_input
        except ValueError as e:
            print(e)


def newId(*args):
    id = 0
    for i in args:
        for j in i:
            if j['id'] > id:
                id = j['id']
    return id + 1


def new_item_laptop(arr, path):
    arr = arr

    id = newId(laptops_all, printers_all, monitors_all)
    model = get_input_text('Введіть model: ')
    processor = get_input_text('Введіть processor: ')
    ram = get_input_text('Введіть ram: ')
    storage = get_input_text('Введіть storage: ')
    display = get_input_text('Введіть display: ')
    price = get_input_number('Введіть price: ')
    quantity = get_input_number('Введіть quantity: ')
    arr.append({
        "id": id,
        "model": model.strip(),
        "processor": processor.strip(),
        "ram": ram.strip(),
        "storage": storage.strip(),
        "display": display.strip(),
        "price": price,
        "quantity": quantity
    })

    buy_question = [
        {
            "type": "confirm",
            "message": f'''
    Чи бажаєте додати товар:
        №{id} модель: {model}.
        Характеристики:
            процесор:           {processor}
            оперативна памʼять: {ram}
            сховище:            {storage}
            дисплей:            {display}
            ціна:               ${price}
            кількість:          {quantity}
            ''',

            "name": "confirm_buy",
            "default": True,
        }
    ]
    confirm_buy = prompt(buy_question)['confirm_buy']
    if confirm_buy:
        save_list_to_file(path, arr)
        print("Товар успішно додано.")
    else:
        print("Операція відмінена.")


def new_item(arr, path):
    arr = arr

    id = newId(laptops_all, printers_all, monitors_all)
    model = get_input_text('Введіть model: ')
    specifications = get_input_text('Ведіть характеристики: ')
    price = get_input_number('Введіть price: ')
    quantity = get_input_number('Введіть quantity: ')
    arr.append({
        "id": id,
        "model": model.strip(),
        "specifications": specifications.strip(),
        "price": price,
        "quantity": quantity
    })

    buy_question = [
        {
            "type": "confirm",
            "message": f'''
    Чи бажаєте додати товар:
        №{id} модель: {model}.
        Характеристики:     {specifications}
        ціна:               ${price}
        кількість:          {quantity}
            ''',

            "name": "confirm_buy",
            "default": True,
        }
    ]
    confirm_buy = prompt(buy_question)['confirm_buy']
    if confirm_buy:
        save_list_to_file(path, arr)
        print("Товар успішно додано.")
    else:
        print("Операція відмінена.")


def selling(arr, path):
    choices = arr
    questions = [
        {"type": "list", "message": "Оберіть товар:", "name": "selected_item", "choices": [
            f"{choice['id']}. {choice['model']}" for choice in choices]}
    ]

    answers = prompt(questions)['selected_item']
    selected_object = next(choice for choice in choices if f"{
                           choice['id']}. {choice['model']}" == answers)
    match selected_object:
        case {"id": id, "model": model, "specifications": specifications, "price": price, "quantity": quantity}:
            print(f"Ви обрали: {model}, Ціна: {
                  round(price * kurs, 2)}, Кількість: {quantity}")

            buy_question = [
                {
                    "type": "confirm",
                    "message": f"Чи бажаєте придбати товар {selected_object['model']}?",
                    "name": "confirm_buy",
                    "default": True,
                }
            ]

            confirm_buy = prompt(buy_question)['confirm_buy']

            if confirm_buy:
                selected_object['quantity'] -= 1
                if selected_object['quantity'] == 0:
                    choices.remove(selected_object)

                print("Товар успішно придбано.")
            else:
                print("Операція відмінена.")
            with open(path, 'w') as file:
                json.dump(choices, file, indent=4)

################### Робота із таблицею ###################


def space_row():
    print(chr(9474), end='')
    for i in range(4):
        print(f'{'':^{space[i]}}', end='', sep='')
        print(chr(9474), end='')
    print()


def table_section():
    print(chr(9500), end='')
    for i in range(3):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9532), end='')
    for i in range(space[3]):
        print(chr(9472), end='')
    print(chr(9508))


def table_title():
    print(chr(9484), end='')
    for i in range(3):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9516), end='')
    for i in range(space[3]):
        print(chr(9472), end='')
    print(chr(9488))

    space_row()

    title = ['Назва товару', 'Характеристики', 'Ціна', 'Наявність']
    count = 0

    for i in title:
        print(chr(9474), end='')
        print(f'{i:^{space[count]}}', end='', sep='')
        count += 1
    print(chr(9474))
    space_row()
    table_section()


def table_end():
    print(chr(9492), end='')
    for i in range(3):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9524), end='')
    for i in range(space[3]):
        print(chr(9472), end='')
    print(chr(9496))


def table_item_laptop(arr, sort='id'):
    sorted_arr = sorted(arr, key=lambda x: x[sort])
    table_title()

    for items in sorted_arr:
        item = ['model', 'processor', "price", "quantity"]
        count = 0
        for i in item:
            print(chr(9474), end='')
            print(f'{items[i]:^{space[count]}}', end='', sep='')
            count += 1
        print(chr(9474), end='')
        print()
        stat = ["ram", "storage", "display"]
        count = 0
        for i in stat:
            print(f'{chr(9474)}{'':^{space[0]}}{chr(9474)}', end='', sep='')
            print(f'{items[i]:^{space[1]}}', end='', sep='')
            print(f'{chr(9474)}{'':^{space[2]}}', end='', sep='')
            print(f'{chr(9474)}{'':^{space[3]}}{chr(9474)}', end='', sep='')
            print()
            count += 1
        if items == arr[len(arr) - 1]:
            table_end()
        else:
            table_section()


def table_item_all(arr, sort='id'):
    sorted_arr = sorted(arr, key=lambda x: x[sort])
    table_title()

    for items in sorted_arr:
        item = ['model', 'specifications', 'price', 'quantity']
        count = 0
        for i in item:
            print(chr(9474), end='')
            print(f'{items[i]:^{space[count]}}', end='', sep='')
            count += 1
        print(chr(9474), end='')
        print()
        if items == arr[len(arr) - 1]:
            table_end()
        else:
            table_section()


space = [30, 40, 15, 11]

##########################################################


def read_list_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Creating a new list.")
        return []


def save_list_to_file(file_name, arr):
    with open(file_name, 'w') as file:
        json.dump(arr, file, indent=4)


laptops_all = read_list_from_file('./data/laptops.json')
printers_all = read_list_from_file('./data/printers.json')
monitors_all = read_list_from_file('./data/monitors.json')

newId(laptops_all, printers_all, monitors_all)

################### Вивід інформації ###################
print('Вітаю в магазині компʼютерної техніки!')
while True:

    questions = [
        {"type": "list", "message": "Зробіть свій вибір:", "name": "value",
            "choices": ['1. Режим продажу;', '2. Режим відображення;', '3. Додати новий продукт;', 'Вихід;']},
    ]

    answers = prompt(questions)['value']

    match answers:
        case '1. Режим продажу;':
            questions = [
                {"type": "list", "message": "Зробіть свій вибір:", "name": "value",
                    "choices": ['1. Ноутбуки;', '2. Принтери;', '3. Монітори;']},
            ]
            answers = prompt(questions)['value']
            match answers:
                case '1. Ноутбуки;':
                    choices = laptops_all
                    questions = [
                        {"type": "list", "message": "Оберіть товар:", "name": "selected_item", "choices": [
                            f"{choice['id']}. {choice['model']}" for choice in choices]}
                    ]

                    answers = prompt(questions)['selected_item']
                    selected_object = next(choice for choice in choices if f"{
                                           choice['id']}. {choice['model']}" == answers)
                    match selected_object:
                        case {"id": id, "model": model, "processor": processor, "ram": ram, "storage": storage, "display": display, "price": price, "quantity": quantity}:
                            print(f"Ви обрали: {model}, Ціна: {
                                  round(price * kurs, 2)}, Кількість: {quantity}")

                            buy_question = [
                                {
                                    "type": "confirm",
                                    "message": f"Чи бажаєте придбати товар {selected_object['model']}?",
                                    "name": "confirm_buy",
                                    "default": True,
                                }
                            ]

                            confirm_buy = prompt(buy_question)['confirm_buy']

                            if confirm_buy:

                                selected_object['quantity'] -= 1

                                if selected_object['quantity'] == 0:
                                    choices.remove(selected_object)

                                print("Товар успішно придбано.")
                            else:
                                print("Операція відмінена.")
                            with open('./data/laptops.json', 'w') as file:
                                json.dump(choices, file, indent=4)
                case '2. Принтери;':
                    selling(printers_all, './data/printers.json')
                case '3. Монітори;':
                    selling(monitors_all, './data/monitors.json')
            continue
        case '2. Режим відображення;':
            print('Що вас цікавить?')
            questions = [
                {"type": "list", "message": "Оберіть трикутник:", "name": "value",
                    "choices": ['1. Ноутбуки;', '2. Принтери;', '3. Монітори;']},
            ]
            answers = prompt(questions)['value']
            match answers:
                case '1. Ноутбуки;':
                    table_item_laptop(laptops_all)
                    while True:
                        questions = [
                            {"type": "list", "message": "Відсортувати товар?",
                                "name": "value", "choices": ['1. Так;', '2. Ні;']},
                        ]
                        answers = prompt(questions)['value']
                        match answers:
                            case '1. Так;':
                                questions = [
                                    {"type": "list", "message": "По чому бажаєте відсортувати?",
                                        "name": "value", "choices": ['1. Ціна;', '2. Модель;', '3. Процесор;', '4. Оперативна памʼять;', '5. Сховище;', '6. Дисплей']},
                                ]
                                answers = prompt(questions)['value']
                                match answers:
                                    case '1. Ціна;':
                                        table_item_laptop(laptops_all, 'price')
                                        continue
                                    case '2. Модель;':
                                        table_item_laptop(laptops_all, 'model')
                                        continue
                                    case '3. Процесор;':
                                        table_item_laptop(
                                            laptops_all, 'processor')
                                        continue
                                    case '4. Оперативна памʼять;':
                                        table_item_laptop(laptops_all, 'ram')
                                        continue
                                    case '5. Сховище;':
                                        table_item_laptop(
                                            laptops_all, 'storage')
                                        continue
                                    case '6. Дисплей':
                                        table_item_laptop(
                                            laptops_all, 'display')
                                        continue
                            case '2. Ні;':
                                break
                        break

                case '2. Принтери;':
                    while True:
                        table_item_all(printers_all)
                        while True:
                            questions = [
                                {"type": "list", "message": "Відсортувати товар?", "name": "value",
                                 "choices": ['1. Так;', '2. Ні;']},
                            ]
                            answers = prompt(questions)['value']
                            match answers:
                                case '1. Так;':
                                    questions = [
                                        {"type": "list", "message": "По чому бажаєте відсортувати?", "name": "value",
                                         "choices": ['1. Ціна;', '2. Модель;']},
                                    ]
                                    answers = prompt(questions)['value']
                                    match answers:
                                        case '1. Ціна;':
                                            table_item_all(
                                                printers_all, 'price')
                                            continue

                                        case '2. Модель;':
                                            table_item_all(
                                                printers_all, 'model')
                                            continue

                                case '2. Ні;':
                                    break
                        break
                case '3. Монітори;':
                    while True:
                        table_item_all(monitors_all)
                        while True:
                            questions = [
                                {"type": "list", "message": "Відсортувати товар?", "name": "value",
                                 "choices": ['1. Так;', '2. Ні;']},
                            ]
                            answers = prompt(questions)['value']
                            match answers:
                                case '1. Так;':
                                    questions = [
                                        {"type": "list", "message": "По чому бажаєте відсортувати?", "name": "value",
                                         "choices": ['1. Ціна;', '2. Модель;']},
                                    ]
                                    answers = prompt(questions)['value']
                                    match answers:
                                        case '1. Ціна;':
                                            table_item_all(
                                                monitors_all, 'price')
                                            continue
                                        case '2. Модель;':
                                            table_item_all(
                                                monitors_all, 'model')
                                            continue
                                case '2. Ні;':
                                    break
                        break
            continue
        case '3. Додати новий продукт;':
            questions = [
                {"type": "list", "message": "Зробіть свій вибір:", "name": "value",
                 "choices": ['1. Додати ноутбук:', '2. Додати принтер;', '3. Додати монітор;', 'Вихід;']},
            ]
            answers = prompt(questions)['value']

            match answers:
                case '1. Додати ноутбук:':
                    new_item_laptop(laptops_all, './data/laptops.json')
                case '2. Додати принтер;':
                    new_item(printers_all, './data/printers.json')
                case '3. Додати монітор;':
                    new_item(monitors_all, './data/monitors.json')

            continue

        case 'Вихід':
            break
    break
#########################################################
