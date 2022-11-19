print("**********PROGRAMMED BY:**********")
print("*******Pauline Joy R. Mingo*******")


#Variables

#Loop
while True: 
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    even = 0
    x = 0
    for x in range (start, end, 1): 
        if (x%2) == 0:
            even = even +x

    print("The starting and the ending number is: ", start, end)
    print("The sum of evens are ", even)        




