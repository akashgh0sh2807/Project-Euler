# Created a variable in which we'll add all the multiples.
Sum_of_multiples = 0
# Created a loop to run upto 1000.
for i in range(1, 1000, 1):
    """ Applying a condition that if 
    remainder is 0 after dividing by 3 or 5 
    then, the no. added to our variable."""
    if i % 3 == 0 or i % 5 == 0:
        Sum_of_multiples += i
# Printing our final value.
print("The addition of all multiples of 3 and 5 are:", Sum_of_multiples)
