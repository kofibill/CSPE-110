print('Welcome to the guessing game!!\n')
secret='raptor'
print('You hint is:_ _ _ _ _ _ \n')
guess=''
guess_count=1
while guess!=secret:
    
    guess=input('What is your guess? ')
    guess_count=guess_count + 1

    if len(guess)!=len(secret):
       print('Sorry, your guess should be the same number letter as the secret word.\n')
    else:
        print('Your hint is _ _ _ _ _ _\n')

    for  letter in guess:
        if secret==guess:
         print (letter.upper(),end='')
         
        elif letter in secret:
         print (letter.lower(), end='')

        else:
         print('_', end='')


print('You guess the correct word.\n')
print(f'It took you {guess_count} guess(es)')