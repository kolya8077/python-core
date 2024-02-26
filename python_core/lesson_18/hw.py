import json


def space_row():
    print(chr(9474), end='')
    for i in range(4):
        for j in range(space[i]):
            print(' ', end='')
        print(chr(9474), end='')
    for i in range(space[4]):
        print(' ', end='')
    print(chr(9474))


space = [6, 12, 27, 16, 15]

title = [
    2,
    "No",
    2,
    4,
    "Item",
    4,
    8,
    'Description',
    8,
    4,
    'Quantity',
    4,
    5,
    'Price',
    5,
]

arr_title = ['number', 'item', 'description', 'quantity', 'price']

arr_space = [6, 12, 23, 16, 15]

stop_execution = False

# Функція для зчитування списку з файлу


def read_list_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Creating a new list.")
        return []

# Функція для збереження списку у файл


def save_list_to_file(file_name, arr):
    with open(file_name, 'w') as file:
        json.dump(arr, file, indent=4)


# Зчитуємо список з файлу або створюємо новий
arr = read_list_from_file('python_core/lesson_18/data.json')

while not stop_execution:
    print(chr(9484), end='')
    for i in range(4):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9516), end='')
    for i in range(space[4]):
        print(chr(9472), end='')
    print(chr(9488))

    space_row()

    i = 0
    while i <= len(title)-1:
        print(chr(9474), end='')
        for j in range(title[i]):
            print(' ', end='')
        i += 1
        print(title[i], end='')
        i += 1
        for k in range(title[i]):
            print(' ', end='')
        i += 1
    print(chr(9474))

    space_row()

    print(chr(9500), end='')
    for i in range(4):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9532), end='')
    for i in range(space[4]):
        print(chr(9472), end='')
    print(chr(9508))

    space_row()

    for e in arr:
        for i, key in enumerate(arr_title):
            print(chr(9474), end='')

            if key == "price":
                formatted_price = f'$ {float(e[key]):6.2f}'
                print(f'{formatted_price:^{arr_space[i]}}', end='', sep='')
            elif key == 'description':
                for j in range(4):
                    print(' ', end='')
                print(f'{e[key]:<{arr_space[i]}}', end='', sep='')

            else:
                print(f'{e[key]:^{arr_space[i]}}', end='', sep='')
        print(chr(9474))

    for i in range(13 - len(arr)):
        space_row()

    print(chr(9500), end='')
    for i in range(4):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9532), end='')
    for i in range(space[4]):
        print(chr(9472), end='')
    print(chr(9508))

    space_row()

    v = 0
    q = 0
    p = 0
    for e in arr:
        for i, key in enumerate(['number', 'item', 'description', 'quantity', 'price']):
            if key == 'number':
                if v < int(e[key]):
                    v = int(e[key])
            elif key == 'quantity':
                q += int(e[key])
            elif key == 'price':
                p += float(e[key])

    if arr:  # Перевірка чи список arr не порожній
        for e in arr[0]:
            for i, key in enumerate(['number', 'item', 'description', 'quantity', 'price']):
                print(chr(9474), end='')
                match key:
                    case 'number':
                        print(f'{v:^{arr_space[i]}}', end='', sep='')
                    case 'item':
                        print(f'{'':^{arr_space[i]}}', end='', sep='')
                    case 'description':
                        for j in range(4):
                            print(' ', end='')
                        print(f'{'':^{arr_space[i]}}', end='', sep='')
                    case 'quantity':
                        print(f'{q:^{arr_space[i]}}', end='', sep='')
                    case "price":
                        print(f'{p:^{arr_space[i]}}', end='', sep='')
            print(chr(9474))
            break

    space_row()

    print(chr(9492), end='')
    for i in range(4):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9524), end='')
    for i in range(space[4]):
        print(chr(9472), end='')
    print(chr(9496))

    while True:
        quest = input('Want to supplement the plate? YES - y or NO - n: ')

        if quest.lower() == 'y':
            while True:
                item = input("Enter item: ")
                description = input("Enter description: ")
                quantity = input("Enter quantity: ")
                price = input("Enter price: ")

                if not item or not description or not quantity or not price:
                    break

                v += 1
                v = str(v)

                arr.append({
                    'number': v.strip(),
                    'item': item.strip(),
                    'description': description.strip(),
                    'quantity': quantity.strip(),
                    'price': price.strip(),
                })

                save_list_to_file('data.json', arr)
                break

            break
        elif quest.lower() == 'n':
            stop_execution = True
            break
        else:
            continue
