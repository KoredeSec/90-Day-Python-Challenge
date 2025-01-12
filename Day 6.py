#Program that takes a list of numbers and prints the sum and average
numbers = []
total = 0

while True:
    number = int(input("Please input a number (Enter 0 to exit): "))
    if number == 0:
        break
    else:
        numbers.append(number)
        print(numbers)
total = sum(numbers)
average = sum(numbers) / len(numbers)
print(f"The total is: {total}")
print(f"The average is: {average}")
