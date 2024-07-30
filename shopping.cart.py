items = []
prices = []
user_item = None
user_price = -1


# while user_item != 'done':
   
if user_item != 'done':
        user_item = input('What item would you like to add? ')
        items.append(user_item)

        user_price = input(f"What is the price of '{user_item}'? ")
            

print(f"'{user_item}' has been added to the cart.")
    
