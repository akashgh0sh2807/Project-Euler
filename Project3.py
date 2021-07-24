# Created a function to find largest prime.
def largest_prime(number):
    # Assigned 2 because 1 is universal prime.
    i = 2
    # Running a loop till i is greater than number.
    while i < number:
        ''' Applied a condition that
        if number is divisible by i then divide it
        else increase i with 1 and return the number.'''
        if number % i == 0:
            number //= i
        else:
            i += 1
    return number


# Printed the largest prime divisor.
print("Largest prime factor of 600851475143 is:", largest_prime(600851475143))
