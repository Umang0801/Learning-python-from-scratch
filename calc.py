from helper import add, subtract, multiply, divide

while True:
   print('Welcome to the simple calculator')
   print('Select an operation:')
   print('1. Add', '2. Subract', '3. Multiplication', '4. Division', '5. Quit')

   choice = input('Enter choice: ').strip() .lower()

   a = int(input('Enter the first number: '))
   b = int(input('Enter the second number: '))

   if choice == '1' or choice == 'one':
        print(f'{add(a, b)}')
   elif choice == '2' or choice == 'two':
        print(f'{subtract(a, b)}')
   elif choice == '3' or choice == 'three':
        print(f'{multiply(a, b)}')
   elif choice == '4' or choice == 'four':
        print(f'{divide(a, b):.3f}')
   else:
        print('Invalid option.')

   if choice == '5' or choice == 'five':
      print('Exiting the calculator')
      break