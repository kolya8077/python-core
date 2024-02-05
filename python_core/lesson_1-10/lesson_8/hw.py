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


arr = [
    {'number' : '1','item' : 'P196', 'description': 'Sansung Color TV', 'quantity' : '1', 'price' : '829.00'},
    {'number' : '2','item' : 'P020', 'description': 'Uniden Handset', 'quantity' : '1', 'price' : '29.00'},
    {'number' : '3','item' : 'p111', 'description': 'Folder Blank', 'quantity' : '1', 'price' : '2.70'},
    ]

arr_title = ['number', 'item', 'description', 'quantity', 'price' ]

arr_spase = [6,12,23,16,15]

stop_execution = False

while not stop_execution:
    #1
    print(chr(9484), end='')
    for i in range(4):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9516), end='')
    for i in range(space[4]):
        print(chr(9472), end='')
    print(chr(9488))
    #2
    space_row()
    #3
    i = 0
    while i <= len(title)-1:
        print(chr(9474), end='')
        for j in range(title[i]):
            print(' ', end='')
        i+=1
        print(title[i], end='')
        i+=1
        for k in range(title[i]):
            print(' ', end='')
        i+=1
    print(chr(9474))
    #4
    space_row()
    #5
    print(chr(9500), end='')
    for i in range(4):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9532), end='')
    for i in range(space[4]):
        print(chr(9472), end='')
    print(chr(9508))
    #6
    space_row()
    
    #7
    for e in arr:
        for i, key in enumerate(['number', 'item', 'description', 'quantity', 'price']):
            print(chr(9474), end='')

            if key == "price":
                formatted_price = f'$ {float(e[key]):6.2f}'
                print(f'{formatted_price:^{arr_spase[i]}}', end='', sep='')
            elif key == 'description':
                for j in range(4):
                    print(' ', end='')
                print(f'{e[key]:<{arr_spase[i]}}', end='', sep='')
                
            else:
                print(f'{e[key]:^{arr_spase[i]}}', end='', sep='')
        print(chr(9474))
    
    #8
    for i in range(13 - len(arr)):
        space_row()
    #9
    print(chr(9500), end='')
    for i in range(4):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9532), end='')
    for i in range(space[4]):
        print(chr(9472), end='')
    print(chr(9508))
    #10
    space_row()
    #11
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
    
    for e in arr[0]:
        for i, key in enumerate(['number', 'item', 'description', 'quantity', 'price']):
            print(chr(9474), end='')
            match key:
                case 'number':
                    print(f'{v:^{arr_spase[i]}}', end='', sep='')
                case 'item':
                    print(f'{'':^{arr_spase[i]}}', end='', sep='')
                case 'description':
                    for j in range(4):
                        print(' ', end='')
                    print(f'{'':^{arr_spase[i]}}', end='', sep='')
                case 'quantity':
                    print(f'{q:^{arr_spase[i]}}', end='', sep='')
                case "price":
                    print(f'{p:^{arr_spase[i]}}', end='', sep='')
        print(chr(9474))
        break
    
    space_row()
    #13
    print(chr(9492), end='')
    for i in range(4):
        for j in range(space[i]):
            print(chr(9472), end='')
        print(chr(9524), end='')
    for i in range(space[4]):
        print(chr(9472), end='')
    print(chr(9496))
    
    #Мої додуми))
    while True:
        quest = input('Want to supplement the plate? YES - y or NO - n:  ')

        match quest:
            case 'y':
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
                    break
                break
            case 'n':
                stop_execution = True
                break
            case _:
                continue