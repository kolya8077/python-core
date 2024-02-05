brickWidth = int(print('Ширина цеглини: '))
brickHeight = int(print('Висота цеглини: '))

holeWidth = int(print('Ширина отвору: '))
holeHeight = int(print('Висота отвору: '))

if brickWidth == holeWidth and brickHeight == holeHeight:
  print('Цеглина підходить')
else:
  print('Підберіть іншу цеглину')