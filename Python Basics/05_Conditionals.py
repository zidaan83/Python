'''
# if - do smt if the condition is true
# Else - do smt else

# Exercise 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to sign up") 
elif age < 0:
    print("Please Enter the Valid Age")
else:
    print("You are not eligible to sign up")
'''


# Exercise 2
food = input("Are you hungry? (Yes/No): ")

if food == "Yes":
    print("You should eat something")
else:
    print("Don't eat anything")
    