print ('Hello, welcome to the shopping cart program!!\n')
selections  = []
choice_selection=''
price=[]
price_tag=''
total_price = 0

number_selected = ''
while number_selected != '5':
   print('Please select one of the following:\n')
   menu=[]
   menu.append('1. Add an item')
   menu.append('2. Display cart content')
   menu.append('3. Remove Item')
   menu.append('4. Calculate the cart total')
   menu.append('5. Quit\n')

   for menu in menu:
      print(menu)
   number_selected = input ('Please enter any number above to perform an action :')
   
   if number_selected== '1':
      choice_selection = input('What item would you like to add to the cart? ')
      price_tag=int(input(f'What is the price of {choice_selection}? '))
      print (f'{choice_selection } has been added to the cart.')
     
      selections.append(choice_selection)
      price.append(price_tag)
   
   elif number_selected == '2':
      print('Your cart contains:')
      for (a,b) in zip(selections,price):
         print(f'{a}-${b}')
   
   
   elif number_selected == '3':
      choice_selection = input('Which item would you like to remove from the cart? ')
      print(f'{choice_selection} has been removed from the cart')
      selections.remove(choice_selection)
      price.remove(price_tag)
   
      
   
   elif number_selected == '4':
      
      for price in price:
         total_price += price
      print(f'The total price of the items in cart is: ${total_price:.2f}')         
   
   elif number_selected == '5':
      print('Thanks for shopping with us..We hope you come back another time!!')           
   
   else:
      print('Invalid input')


