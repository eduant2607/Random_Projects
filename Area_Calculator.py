#simple control flow example.
#Not making use of DRY
  
import math

print('Welcome to the Area Calculator!')
print('\n')

#Shape selectrion
while True:
  print('1) Square')
  print('2) Rectangle')
  print('3) Triangle')
  print('4) Circle')
  print('5) Quit')
  print('\n')

#Asks the user to pick a shape
  shape = int(input('Please select your option: '))
  print('\n')

#Trying to add a while to make the user select
#An option from the menu
  while shape < 1 or shape > 5:
    print('Invalid option')
    shape = int(input('Please select your shape: '))
    print('\n')

  if shape == 1:
    print('Shape selected: Square')  
    print('\n')
    side  = float(input('Side: '))
    print('\n')
    area = side*side
    print(f'Area: {area}')
    print('\n')
  elif shape == 2:
    print('Shape selected: Rectangle')
    print('\n')
    length = float(input('Length: '))
    width = float(input('Width: '))
    print('\n')
    area = length*width
    print(f'Area: {area}')
    print('\n')
  elif shape == 3:
    print('Shape selected: Triangle')
    print('\n')
    base = float(input('Base: '))
    height = float(input('Height: '))
    print('\n')
    area = (base*height)/2
    print(f'Area: {area}')
    print('\n')
  elif shape == 4:
    print('Shape selected: Circle')
    print('\n')
    radius = float(input('Radius: '))
    print('\n')
    area = math.pi*(radius**2)
    print(f'Area: {area}')
    print('\n')
  elif shape == 5:
    print('Program terminated!')
    break

