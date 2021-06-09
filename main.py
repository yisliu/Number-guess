import random

def game():
  turns = 1
  hint = 0
  num = random.randint(1,10)
  print("-----------------------------------")
  print("Welcome to my number guessing game!")
  print("-----------------------------------")
  print(num)
  guess = input("Guess a number from 1 to 10: ")
  while turns<10:
    if int(guess) == num:
      print("You guessed the right number!")
      print("You tried: " + str(turns) + " time.")
      print("You used " + str(hint) + " hints")
      turns = 10
    else:
      if int(guess)<num:
        print("It is not " + guess)
        print("try again")
        guess = input("Hint: it is bigger than your guess.")
        hint = hint + 1
        turns = turns + 1
      elif int(guess)>num:
        print("Your guess is wronge.")
        print("try again")
        guess = input("Hint: the number is smaller than your guess")
        hint = hint + 1
        turns = turns + 1

game()