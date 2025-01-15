#program that takes user input for a number and catches errors if the user inputs something invalid (non-integer).
try:
    number = int(input("How old are you?: "))
    print(f"You are {number} years old!")
except ValueError:
    print("Input only numbers please!")