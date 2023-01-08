import random

#generate a random number between 1 and 10
random_number = random.randint(1,100)

#store the number of guesses
guesses_taken = 0

#prompt the user to guess the number
print('Guess a number between 1 and 100')

#loop until the user guesses the correct number
while guesses_taken < 5:
    #get the user's guess
    guess = int(input())
    guesses_taken += 1

    #check if the guess is correct
    if guess == random_number:
        print('You guessed correctly!')
        break
    else:
        #give the user a hint
        if guess < random_number:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')

#if the user has taken 5 guesses, tell them they lost
if guesses_taken == 5:
    print('You lost! The number was ' + str(random_number))
