def calculator(n1, n2, type):
    
    if type =='sum': return n1 + n2
    elif type == 'subtract': return n1 - n2
    elif type == 'multiply': return n1 * n2
    elif type == 'division': return n1 / n2
    elif type == 'squareroot': return n1 ** 0.5
    elif type == 'raiseto': return n1 ** n2
    elif type == 'percentage': return (n1*n2)/100
    
    else:
        print('Calulator does not support that function yet')

if __name__ == '__main__':

    type=str(input("What to do?: "))
    # if squareroot is chosen, ask for n1 only
    if type == 'squareroot':
        n1 = int(input("Enter the number to find the square root of: "))
        n2 = 0 
    else:
        n1 = int(input("Number 1: "))
        n2 = int(input("Number 2: "))
    
    number = calculator(n1=n1, n2=n2, type=type)

    if number is not None:
        print(f"Voila! Your Number is {number:.3f}")