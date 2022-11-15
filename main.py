order = input("What is your name? ")
if order == "Charles" or order == "charles":
  print("So you were born June 14?.")
  cheese = input("Do you play basketball?")
  if cheese == "yes":
    print("Boy you 42 so barely!.")
  else: 
    print("Quitter.")
elif order == "Kameron" or order == "kameron":
  print("The greatest tennis player alive eh?")
  toppings = input("Do you smoke weed?")
  if toppings == "yes":
    print("My ninja!")
  else:
    print("Well aren't you lame.")
elif order == "Kymberlee" or  order == "Kym":
  print("The sarcastic one I see..")
  scope = input("What is your sign?")
  if scope == "Leo":
    print("You LION you!")
  else:
    print("You're lying.")
elif order == "Brooke":
  print("Congrats on the baby boy")
  baby = input("What are you going to name that baby?")
  if baby == "I don't know":
    print("Get it togeher")
  else:
    print("Oh ok, I guess")
elif order == "Dana" or order == "dana":
  print("Hello Gigi")
  tatum = input("Did JJ complete his homework?")
  if tatum == "Yes" or tatum == "yes":
    print("That's good")
  else:
    print("You're slacking grandmother")
elif order == "Cortina" or order == "Tina":
  print("Hello Tina!")
  wallace = input("Have you completed your midterm yet?")
  if wallace == "Yes" or wallace == "yes":
    print("Ok I see you")
  else:
    print("Well why not?")
    
import random
number = random.randint(1, 10)

player_name = input("Sorry, what's your name again?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))  
