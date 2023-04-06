# Prompt the user to enter an n-digit number
x = input("Enter an n-digit number: ")

# Convert the input string to a list of digits
digits = [int(digit) for digit in x]

# Calculate the sum of the digits using the built-in sum() function
digit_sum = sum(digits)

# Print the sum of the digits
print("The sum of the digits is:", digit_sum)
