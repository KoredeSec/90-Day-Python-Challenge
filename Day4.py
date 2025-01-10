import time

countdown = int(input("Enter the time in seconds: "))

for x in range(0, countdown):
    print(x)
    time.sleep(1)

print("Happy new year!")