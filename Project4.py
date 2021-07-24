# Created a variable to store the biggest palindrome value.
biggest_palindrome = 0
# Created a range to multiply with other range.
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        # Created a variable to store the product of two ranges.
        product = i * j
        ''' Applied a condition to check
         reverse of product is equal to reverse or not
         and also bigger than biggest palindrome.'''
        if (str(product) == str(product)[::-1]) and biggest_palindrome < product:
            biggest_palindrome = product
# Printing the largest palindrome made from the product of 3-digit no.
print("The largest palindrome made from the product of 3-digit numbers is:", biggest_palindrome)
