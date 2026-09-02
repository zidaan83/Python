
# input() - a function that takes input from user and return entered data as string 

name = input("What is your name: ")
age = int(input("What is your age: "))

age = age + 1

print(f"Happy Birthday {name}")
print(f"You are {age} years old")



# Exercise - Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"the area is {area} cm²")
