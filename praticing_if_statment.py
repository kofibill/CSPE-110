import numbers


number1=int(input('Please enter a number: '))
number2=int(input('Please enter another number: '))
if number1>number2:
    print('The first number is greater')
else:
    print('The first number is not greater')
if number1==number2:
    print('The numbers are equal')
else:
    print('The numbers are not qeual')
if number2>number1:
    print('The second number is greater')
else:
    print('The second number is not greater')
print()    
animal=input('Please enter your favorite animal: ')
if animal.capitalize()=='Dog':
    print('That\'s my favorite animal too!')
else:
    print('That\'s not my favorite animal!')