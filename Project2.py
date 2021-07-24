""" Created three variable, one to store the additions,
and the other two to start Fibonacci series."""
sum_of_even, a, b = 0, 1, 2
# Applied a loop upto 4 million.
while a <= 4000000:
    # Started creating next no. in series by adding first two.
    c = a + b
    # Swapping the values.
    a, b = b, c
    # Applied condition to add only even no. which are easily divisible by 2.
    if a % 2 == 0:
        sum_of_even += a
# Printing the result.
print("The sum of all even numbers in Fibonacci series are:", sum_of_even)
