
number = int(input("Give me a number: "))
x = range(1,number+1)
divine = []
for elem in x:
    if number % elem == 0:
        divine.append(elem)

print(divine)
