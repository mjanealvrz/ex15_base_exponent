#  Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# Pseudocode
# Set variable for base and exponent and store values
base_value= 5
exponent_value= 4

# Create a function to calculate the exponentiation
def exponent():
    # Calculate the result of base raised to the power of exp
     result = base_value ** exponent_value
    # Return the calculated result
     return result 
# Set result to call  exponent with parameters base value and exponent value
result = exponent(base_value, exponent_value)
# Print result
print(f"The {base_value} raised to the power of {exponent_value} is: {result}")