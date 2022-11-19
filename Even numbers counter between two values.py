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

    print()
    print("The starting and the ending number is: ", start, end)
    print()
    print("The sum of evens are ", even)        
    print()

    yes = input("Would you like to run the program again? (y/n) ")
    if yes == "y":
        continue
    else:
        break
    
    
print("Done :)")
1




