# Write a function called divisible_by_7. 
# This function must take an integer as a parameter.
# This function must return True if the passed integer
# is divisible by 7 or false if not.
# Note, you should not prompt the user for input. 

def divisible_by_7(num):
    if num % 7 == 0:
       return True
    else:
       return False

# Write a function called compare_it that takes two parameters. 
# You should first test if both parameters are integers.
# If not, return False
# Then you should test if the parameters are equal.
# If they are not, return False
# Finally, test if the parameters are greater than zero.
# If they are not, return False.
# If all of these tests pass, return True.

def compare_it (para1, para2):
   if not isinstance(para1, int) or not (para2, int):
      return False

   if para1 == para2:
      return False

   if para1 < 0 and para2 < 0:
      return False

   return True



# Write a function called keyword_counter that takes three parameters
# Parameter one should be a list of words.
# The second should be a Boolean
# The third should be either a string or a filename
# The first parameter is your list of keywords.
# The second parameter if set to True means that the third parameter is a string
# The second parameter if set to False means that the third parameter is a filename
# In both cases, you will need to read a string and count occurrences of each
# keyword in that string. If the third parameter is a string, you can use that
# directly. If it is a filename, then you need to read the contents of a file
# into a string first. Then search for occurrences.
# Your function must return a dictionary with the keywords as the key and the 
# count of occurrences of that keyword as the value. 
# Since this is tricky, I've given you the code to read from a file that you'll
# need to include in your function.
# NOTE: Your test should not be case sensitive so if
# one of the words is "fish" your function should count 
# "fish", "Fish", "FISH" or any other combination of 
# capitalization as an occurrence. 
with open(file_name, "r") as f:
   text = f.read().replace("\n", " ")


def keyword_counter(hey, hi, yo_file):
   if yo_file:



