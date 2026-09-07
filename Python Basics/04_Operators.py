# Operators are symbols/keywords used to perform operations on values and variables

# 1 - Arithmetic Operator
# Used for mathematical calculations

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor Division
print(a % b)   # Modulus/Remainder
print(a ** b)  # Exponent/Power



# 2 - Comparision operator 
# used to compare two values
# the result is always True or False

age = 20

print(age == 20)   # Equal to
print(age != 20)   # Not Equal to
print(age > 18)    # Greater than
print(age < 18)    # Smaller than
print(age >= 20)   # Greater than or Equal to
print(age <= 20)   # Smaller than or Equal to



# 3 - Assignment Operators
# Used to assign/update values

x = 10

x += 5
print(x)    

x *= 2
print(x)  


# 4 Logical operator
# Used to combine conditions
# there are three types:

# and - Both conditions must be True
age = 20
print(age > 18 and age < 25)

# or - At least one condition must be True
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outside event is cancelled")
else:
    print("The outside event is still scheduled")

# not - Reverses the result
temp = 24
is_sunny = False

if 25 > temp > 0 and not is_sunny:
    print("It is sunny outside")
else:
    print("It is not sunny outside")