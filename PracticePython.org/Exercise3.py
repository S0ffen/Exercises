a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""
Extra 1
"""
numberBelow5 = []
for numbers in a:
    if numbers < 5:
        numberBelow5.append(numbers)

print(numberBelow5)

"""
Extra 2
"""

print( [number for number in a if number < 5] )

"""
Extra 3
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Please provide a number: "))
print([y for y in a if y < number])