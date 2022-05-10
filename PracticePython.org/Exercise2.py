number = int(input("What is your number: "))
if number % 2 == 0:
    print("you picked a even number")
elif number % 2 == 1:
    print("you picked a odd number")

"""
Extra 1
"""

if number % 4 == 0:
    print("Your number is even and it can be divided 4")

"""
Extra 2
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
num = int(input("What is your first number: "))
check = int(input("What is your second number: "))

if num % check == 0:
    print("your number divides evenly by", check)
else:
    print("your number does not divides evenly by",check)