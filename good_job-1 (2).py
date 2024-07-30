print ('welcome to the shopping cart program!')
selections  = []
choice_selection=''
price=[]
price_tag=''
total_price = 0

number_selected = ''
while number_selected != '5':
   print('please select one of the following:')
   menu=[]
   menu.append('1. add item')
   menu.append('2. view cart')
   menu.append('3. remove item')
   menu.append('4. compute total')
   menu.append('5. quit')

   for menu in menu:
      print(menu)
   number_selected = input ('please enter an action :')
   
   if number_selected== '1':
      choice_selection = input('what item would you like to add?')
      price_tag=int(input(f'what is the price of {choice_selection}? '))
      print (f'{choice_selection } has been added to the cart.')
     
      selections.append(choice_selection)
      price.append(price_tag)
   
   elif number_selected == '2':
      print('the content of the cart are:')
      for (a,b) in zip(selections,price):
         print(f'{a}-${b}')
   
   
   elif number_selected == '3':
      choice_selection = input('which item would you like to remove?')
      print(f'{choice_selection} has been removed from the cart')
      selections.remove(choice_selection)
      price.remove(price_tag)
   
      
   
   elif number_selected == '4':
      
      for price in price:
         total_price += price
      print(f'the total price of the items in cart is: ${total_price:.2f}')         
   
   elif number_selected == '5':
      print('thank you, have a nice day')           
   
   else:
      print('invalid input')


