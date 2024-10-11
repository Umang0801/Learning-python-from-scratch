import random

print('Welcome!')
print('Think of a number beetween 1 to 100')
input('Hit Enter when you are done thinking...')

lower_limit = 1
higher_limit = 100
attempts = 0

while lower_limit <= higher_limit:
    guess = (lower_limit + higher_limit) // 2
    attempts += 1
    print(f'Is your number {guess}?')

    feedback = input("Type 'higher', 'lower' or 'correct': ")

    if feedback == 'correct':
        print(f'Voila! I guessed yours number in {attempts} attempts!')
        break

    elif feedback == 'higher':
        lower_limit = guess + 1

    elif feedback =='lower':
        higher_limit = guess + 1

    else:
        print("Invalid input. Please type 'higher, 'lower', or 'correct.'")


         
