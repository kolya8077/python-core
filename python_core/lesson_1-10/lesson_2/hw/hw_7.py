print('''
      Завдання 7
Користувач вводить з клавіатури вартість одного ноутбука, їхню кількість і відсоток
знижки. Порахувати загальну суму замовлення.
      ''')

price = int(input('Ціна одного товару: '))
amount = int(input('Кількість товару: '))
discount = int(input('Бонусна карта: '))

if discount != 0:
  price = price - (price / 100 * discount)

price *= amount

print(f'Сумма вашого замовлення становить {int(price)} грошей)')
