print ('Hello, welcome to the shopping cart program!\n')
selections  = []
choice_selection=''
price=[]
price_tag=''
total_price = 0

action_num = ''
while action_num != '5':
   print('Please select one of the following: ')
   menu=[]
   menu.append('1. Add item')
   menu.append('2. View cart')
   menu.append('3. Remove item')
   menu.append('4. Compute total')
   menu.append('5. Quit')

   for menu in menu:
      print(menu)
   number_selected = input ('Please enter any number on the list above to perfom an action: ')
   
   if action_num== '1':
      choice_selection = input('What item would you like to add to the cart? ')
      price_tag=int(input(f'what is the price of {choice_selection}? '))
      print (f'{choice_selection } has been added to the cart.\n')
     
      selections.append(choice_selection)
      price.append(price_tag)
   
   elif action_num == '2':
      print('Your cart contains:')
      for (a,b) in zip(selections,price):
         print(f'{a}-${b}')
   
   
   elif action_num == '3':
      choice_selection = input('Which item would you like to remove from the cart?')
      print(f'{choice_selection} has been removed from the cart')
      selections.remove(choice_selection)
      price.remove(price_tag)
   
      
   
   elif action_num == '4':
      
      for price in price:
         total_price += price
      print(f'The total price of the items in cart is: ${total_price:.2f}')         
   
   elif action_num == '5':
      print('Thank you for shopping with us today, please have a nice day...You are welcome to come back anytime!!')           
   
   else:
      print('Invald choice!!')


