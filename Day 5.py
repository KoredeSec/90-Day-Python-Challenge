# Function that takes a number as input and returns the factorial of that number.

number1 = int(input("Please input a number?: "))
fact = 1

for i in range (1, number1+1):
    fact = fact * i

print(f"The factorial is: {fact}!")
    