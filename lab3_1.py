def sums():

    # Initialize a variable called first_sum and store the sum of
    # 2 and 2
    first_sum = 2 + 2

    # Store to first_sum the value of first_sum times 10
    first_sum = first_sum * 10

    # Initialize a variable called secret and assign it the value
    # of first_sum plus 2
    secret = first_sum + 2

    return secret
    42


def string_manip(first_name):

    # Initialize a variable called name and assign it the
    # parameter.
    name = first_name
    jessica = name
    print(name)
    'Jessica'

    # Use builtin string functions and slices to replace None with
    # the appropriate manipulation of your name. I've done the first one.
    all_caps = name.upper()
    all_lowercase = name.lower()
    first_five_letters = name[:5]
    last_two_letters = name[-2:]


all_caps = name.upper()
all_caps
'JESSICA'
all_lowercase = name.lower()
all_lowercase
'jessica'
first_five_letters = name[:5]
first_five_letters
'Jessi'
last_two_letters = name[-2:]
last_two_letters
'ca'


def greeter_bot():

    # TODO: Use the input() function to prompt the user for their name.
    # Then assign the value to a variable called name and print a greeting.
    # I have started it for you, but you need to modify the input and
    # print functions.
    # Hint: to get the test to pass, the greeting should be "Hello, input name"
    fname = input()
    print()


def greeter_bot():


fname = input("Hello, input name")
print(input)
input
'Hello, input name'


def temp_calculator():

    # Write code that prompts the user for a temperature in degrees
    # celsius and prints the equivalent temperature in degrees fahrenheit.
    # The formula is C = (F - 32) * (5/9).
    # Define a function to convert
    # celsius temperature to Fahrenheit

celsius = float(input("Enter temperature in celsius: ")
'Enter temperature in celsius:' 32

fahrenheit=(celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))
32.00 Celsius is: 89.60 Fahrenheit


def equitable_bill_splitter():

    
#Create the variable people and ask the user to provide an answer in the form of an integer "How many people are paying?"
    people=int(input("How many people are paying? "))
#Create an array stored to the variable salaries 
    salaries=[]
#Create a total variable that will assign value to salaries
    total=0
#create an interation loop for salary of each person formatted to its own index
    for i in range(people):
        sal=int(input("What is the salary of person {}?".format(i+1)))
        total += sal
        salaries.append(sal)

#create a variable total_bill that prompts the user to answer the question "How much is the bill? " 
#if float is not added then the user will have to put the bill total in round numbers. 
    total_bill=int(input("How much is the bill? "))
#process through the loop and return the amount per person to be paied based on the comparison of salary to total expense ratio
    for j in range(len(salaries)):
        print("Person {} should pay ${}\n".format(
            j + 1, round((total_bill * (salaries[j]/total)), 2)))
