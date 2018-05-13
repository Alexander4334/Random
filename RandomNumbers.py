from random import randint

numbers = []
isInt = False
while True:
    amount = raw_input("How many random numbers? ")
    try:
        amount = int(amount)
        break
    except ValueError:
        print "ERROR: Not an integer"
while True:    
    minimum = int(raw_input("What is the minimum value? "))

    try:
        minimum = int(minimum)
        break
    except ValueError:
        print "ERROR: Not an integer"
while True:
    maximum = int(raw_input("What is the maximum value? "))

    try:
        maximum = int(maximum)
        break
    except ValueError:
        print "ERROR: Not an integer"
        
for x in range(amount):
    random = randint(minimum, maximum)
    numbers.append(random)

numbers.sort()
print numbers

