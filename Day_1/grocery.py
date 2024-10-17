grocery = {'Apple': 20, 'Avocado': 40, 'Banana': 10, 'Dragonfruit': 70, 'Guava': 20, 'Kiwi': 40, 'Mango': 20, 'Melon': 30, 'Orange': 20, 'Papaya': 40, 'Pinapple': 150, 'Pomegranate': 20, 'Strawberry': 5, 'Tangerine': 20, 'Watermelon': 40}

print('Welcome to the grocery store!')
items = ', '.join(grocery.keys())
print(f'Available items: {items}.')

cart = []

while True:
     item_needed = input('What do you need? (Type "Done" when finished) ').strip() .capitalize()

     if item_needed == 'Done':
         break

     if item_needed in grocery:
        quantity_needed = int(input(f'How many do you need?\n'))

        #adds the items and quantity to the cart  
        cart.append((item_needed, quantity_needed))

     else:
        print('Sorry, we do not have that item available at the moment.')

total_price = 0
if cart:
    print('Your cart:')
    for item, quantity in cart:
        item_total = grocery[item] * quantity  
        total_price += item_total 
        print(f'- {quantity} {item}: {item_total} INR') 
    
    print(f'The total price for your selected items is: {total_price} INR')
else:
    print('Your cart is empty.')
