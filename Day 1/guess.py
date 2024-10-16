import random

def guess_number():
    print('Welcome!')
    print('Think of a number between 1 to 100')
    input('Press Enter when you are done thinking...')

    lower_limit = 1
    higher_limit = 100
    attempts = 0

    while True:
        guess = random.randint(lower_limit, higher_limit) 
        attempts += 1
        print(f'Is your number {guess}?')

        feedback = input("Type 'higher', 'lower', or 'correct': ")

        if feedback == 'correct':
            print(f'Voila! I guessed your number in {attempts} attempts!')
            break
            
        elif feedback == 'higher':
            lower_limit = guess + 1 
            guess = (lower_limit + higher_limit) // 2

        elif feedback == 'lower':
            higher_limit = guess - 1
            guess = (lower_limit + higher_limit) // 2
         
        else:
            print("Invalid input. Please type 'higher', 'lower, or 'correct'")
            attempts -= 1

guess_number()
