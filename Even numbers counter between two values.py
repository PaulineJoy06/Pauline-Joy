print("**********PROGRAMMED BY:**********")
print("*******Pauline Joy R. Mingo*******")

print()
print("EVEN NUMBER ADDITION CALCULATOR BETWEEN TWO VALUES")
print()

#Create a program that that should first read in two values from the keyboard, a starting value and an ending value. 
# It should sum all the even numbers between those two values including the endpoints and display the sum.

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
    print("The starting and the ending number are: ", start, "and", end)
    print()
    print("The sum of evens are ", even)        
    print()

    yes = input("Would you like to run the program again? (y/n) ")
    if yes == "y":
        continue
    else:
        break
    
print()   
print("Done! Thank you for using this program.")
print()





