print('''
      Завдання 10
Користувач вводить з клавіатури час початку і час завершення використання скутера
(години, хвилини та секунди). Порахувати вартість подорожі, якщо вартість хвилини —
2 гривні.
      ''')

PRICE = 2

startHours = int(input('Введіть години початку: '))
startMinutes = int(input('Введіть хвилини початку: '))
startSeconds = int(input('Введіть секунди початку: '))

endHours = int(input('Введіть години завершення: '))
endMinutes = int(input('Введіть хвилини завершення: '))
endSeconds = int(input('Введіть секунди завершення: '))

startTime = startHours * 3600 + startMinutes * 60 + startSeconds
endTime = endHours * 3600 + endMinutes * 60 + endSeconds

duration = endTime - startTime

trip = (duration / 60) * PRICE

hourse = duration // 3600
minute = duration % 3600 // 60
secund = duration % 60

print(f'Тривалість поїздки: {hourse}годин {minute}хвилин {secund}секунд')
print(f'Вартість подорожі: {trip} гривень')





