number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
number_3 = int(input('Enter the third number: '))

largest_number = number_1

if number_2 > number_1:
    largest_number = number_2

if number_3 > number_1:
    largest_number = number_3

print(f'The largest number among the numbers {number_1}, {number_2} and {number_3} is {largest_number}')