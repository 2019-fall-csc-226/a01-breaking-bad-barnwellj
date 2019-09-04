######################################################################
# Author: Jacob Barnwell      TODO: Change this to your name
# Username: barnwellj              TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
print("Hello, welcome to the zodiac!")
print("What year were you born?: ")
birth_year = input("")


if birth_year == "1999":
    print("1999! You were born in the year of the rabbit!!")
elif birth_year == "2000":
    print("Do you breathe fire? 2000 is the year of the Dragon1!")
elif birth_year == "2001":
    print("Born in the of the SSSSnake!!")
elif birth_year == "2002":
    print("Hey!...is for Horses!")
elif birth_year == "2003":
    print("")
elif birth_year == "2004":
    print("Year of the Monkey! You must like bananas!")
elif birth_year == "2005":
    print("Cock-a-doodle-doo, 2005 is the year of the Rooster! ")
elif birth_year == "2006":
    print("Year of the Dog! I hope your life hasn't been too 'ruff'")
elif birth_year == "2007":
    print("What a Hog!")
elif birth_year == "2008":
    print("AHHH RATS!")
elif birth_year == "2009":
    print("You probably travel in a heard, year of the Ox!")
elif birth_year == "2010":
    print("You are a Tiger, remind me to stay on your good side!")
else:
    print("Only years 1999-2010 are accepted in this program, " + birth_year +
          " is not, please try again")




# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples


######################################################################
# (Required) Task 2# TODO Ask the user for their friend's birth year
#Enter Friends name here Jesse Walker, TA


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
