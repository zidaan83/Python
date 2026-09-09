# while loop - Execute code WHILE condition is true 

# exercise 1
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Your name is: {name}")



# exercise 2
age = int(input("How old are you? "))

while age < 0:
    print("Age Can't be Negative")
    int(input("How old are you? "))

print(f"You are {age} years old")



# Exercise 3
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("Bye!")



# Exercise 4 
num = int(input("Enter a number between 1 - 10: "))

while num < 0 or num > 10:
    print(f"{num} is not valid")
    int(input("Enter a number between 1 - 10: "))

print(f"You chose {num}")



# Exercise 5
i = 0

while i < 5:
    print(i)
    i += 1
    
