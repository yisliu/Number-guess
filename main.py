import random

def game():
  turns = 0
  hint = 0
  num = random.randint(1,10)
  print("-----------------------------------")
  print("Welcome to my number guessing game!")
  print("-----------------------------------")
  print(num)
  guess = input("Guess a number from 1 to 10: ")
  while turns<10:
    if guess == num:
      print("You guessed the right number!")
      print("You tried: " + turns)
      print("You used " + hint + " hints")
      turns = 10
    else:
      if guess<num:
        print("It is not " + guess)
        print("try again")
        print("Hint: it is bigger than your guess.")
        hint = hint + 1
        turns = turns + 1
      elif int(guess)>num:
        print("Your guess is wronge.")
        print("try again")
        print("Hint: the number is smaller than your guess")
        hint = hint + 1
        turns = turns + 1

game()