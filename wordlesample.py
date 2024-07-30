import random
word = ['cat', 'dog', 'pumpkin', 'horse', 'goat', 'chicken', 'turkey', 'candy', 'snow', 'leaf', 'soap', 'soup']
secret = word
guess = ''
guesses = 0
secret = random.choice(word)
print()
print('Welcome to the word guessing game!')
print()
print('Your hint is: ' + '_ ' * len(secret))
print()
while secret != guess:
  print()
  guess = input('What is your guess? ')
  print()
  if len(secret) != len(guess):
    print('Sorry, the guess must have the same number of letters as the secret word.')
    print()
  else:
    for i, letter in enumerate(guess):
    # print(f'{i} {letter} {guess [i]} {secret [i]}')
      if secret [i] == guess [i]:
       print(letter.upper(), end='') 
      elif letter in secret:
       print(letter.lower(), end='')
      else:
       print('_ ', end='')
  guesses = guesses +1
print()   
print('Congratulations! You guessed it!')
print()  
print(f'In only took you {guesses} guesses. ')
print()