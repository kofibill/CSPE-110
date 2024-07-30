print ('welcome to the shopping cart program!')
menu = ['add item', 'view cart' ,'remove item', 'compute total', 'quit']
selections  = []
action = ''
user_selection = ''
prices = []
user_price = ''
total_price = 0

while action != '5':
   print('\nplease select one of the following: ')
   for i in range(len(menu)):
      print(f'{i+1}. {menu[i]}')
   action = input ('please enter an action: ')
   
   if action== '1':
      user_selection = input('what item would you like to add? ')
      user_price  =float(input(f'what is the price of {user_selection}? '))
      print (f'\'{user_selection }\' has been added to the cart.')
     
      selections.append(user_selection)
      prices.append(user_price)
   
   elif action == '2':
      print('the content of the cart are:')
      for i in range(len(selections)):
          item = selections[i]
          price = prices[i]

          print(f'{i+1}. {selections[i]} - ${prices[i]}')
   
   
   elif action == '3':
      remove_item = int(input('What item would you like to remove? '))
      remove_item = remove_item - 1
      selections.pop(remove_item)
      
      print('Item removed')
   
   elif action == '4':
      
      for price in prices:
         total_price += user_price
      print(f'the total price of the items in cart is: ${total_price:.2f}')         
   
   elif action == '5':
      print('Thank you, Goodbye')           
   
   else:
      print('invalid input')


