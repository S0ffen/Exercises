from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Common_Part = set([i for i in b if i in a])
#print(Common_Part)

"""
Extra 1
"""

while True:
    c = [randint(0,500),randint(0,500),randint(0,500),randint(0,500),randint(0,500),randint(0,500)]
    d = [randint(0,500),randint(0,500),randint(0,500),randint(0,500),randint(0,500),randint(0,500)]
    Common_Part_Random = [i for i in c if i in d]
    if len(Common_Part_Random) > 1:
        print(Common_Part_Random)
        print(c)
        print(d)
        break

