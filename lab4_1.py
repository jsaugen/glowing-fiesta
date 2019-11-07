def is_even():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input("Please give me an integer. "))
   out = None
   
   # Create a conditional that sets out to True if the user enters
   # an even integer and False if the user enters an odd integer.

  def is_even():
...    if user_data % 2 == 0:
...       out = True
...    else:
...       out = False
>>> 2 == 2
True
>>> 3 == 0
False
>>> 3 / 2 == 4
False
>>> 4 / 2 == 2
True
>>> 2 == 2
True
  
   # This is for the test.
   return out 

def multi_condition():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input("Please give me an integer. "))

   # Now evaluate the user_data again and have several conditions
   # if the value is zero, print "Don't be such a zero!"
   # if the value is positive and odd, print "Positively odd!"
   # if the value is positive and even, print "Even Steven!"
   # if the value is negative and odd or even, print "Negative Nelly!"
   # remember, with multiple conditions you can use if, elif, elif, else
    if user_data == 0:
...      print("Dont't be such a zero!") 
...   elif user_data % 2 == 0:
...      print("Even Steven!")
...   elif user_data < 0: 
...      print("Negative Nelly!")  
      else:
...      print("Positively Odd!")

   return None


def is_underage():

   # Prompt the user for their age and store it to a variable. Don't
   # forget to convert the input to an integer.
   age = int(input("How old are you? "))
   
   # Set up a conditional with four cases
   # if the age is equal to or above 21, 
   # print "You may drink, smoke, and drive if you wish!"
   # if the age is equal to or above 18 but less than 21, 
   # print "You may smoke and drive!"
   # if the age is equal to or above 16 but less than 18,
   # print "You may drive!"
   # if the age is less than 16, 
   # print "Enjoy your bike, kid!"

>>> def is_underage():     
...   if age >= 21:
...      print("You make drink, smoke, and drive if you wish!")
...   elif age >= 18:    
...      print("You may smoke and drive!")
...   elif age >= 16:
...      print("You may drive!")
...   else:
...      print("Enjoy your bike kid!")
...   return None

def countdown():

# "Bottles of beer on the wall" just for fun and for my own practice :) 
for i in range(99, 0, -1):
        if i == 1:
                print('1 bottle of beer on the wall, 1 bottle of beer!')
                print('So take it down, pass it around, no more bottles of beer on the wall!')
        elif i == 2:
                print('2 more bottles of beer on the wall, 2 more bottles of beer!')
                print('So take one down, pass it around, 1 more bottle of beer on the wall!')
        else:
                print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
                print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))
   
   
   
for i in range(10, -1, -1):
    print(i)

   # Use a loop to print a countdown from 10 to zero with
   # one number on each new line. If you do not use a loop
   # you will not get points for this problem.

   # So the tests fail and they don't throw errors
   return None

def guessing_game(num):
   # This is a guessing game. I have set up a parameter that will be
   # a random integer that your user will have to try to guess.
   # To use num in your condition, you should write something like
   # 
   # if user_input == num: 
   #    
   # You should give your user at most 10 guesses to guess
   # the number. If the guess is too high or too low, you should tell 
   # them "Too High!" or "Too Low!" with the print statement.
   # If they guess the number, you should tell them "You win!"
   # otherwise, if they run out of guesses, tell them, "You lose!"
   # If they want to, your condition should also check for "q" and 
   # if the user enters that the program should exit, saying 
   # "Goodbye, quitter!"
   # No, it's not a very nice program. 


   # So the tests fail and they don't throw errors
   return None

>>> import random
>>> randNum = random.randint(1,100)
>>> guesses = 0
>>> for i in range (1, 10):
...     guesses = guesses + 1
...     print ("Hi Human! Guess a number 1-100! \n")
...     guess = input()
...
...     if guess.isdigit():
...       if int(guess) > randNum:
...         print("your guess is too high \n")
...
...     elif int(guess) < randNum:
...         print("your guess is too low \n")
...
...     elif int(guess) == randNum:
...         print("Duude, you are Genius! \n")
...         print("you needed" + str(guesses) + "guesses")
...
...     else:
...       print("Invalid Input. Try a number. \n")
...
...
Hi Human! Guess a number 1-100!

21

# I researched some number guessing games and found this one. I tried it a few times
# and got it to work! However, I couldn't get any guessing output when I didn't have
# an import statement at the top. Is this something I should always have? Where/How
# do I know what to import and what to assign the name to?
# e.g. in the game above it's:
import random 
randNum = random.randint(1,100)

#Am I missing the import instructions somewhere that's associated with the 
#assignments?