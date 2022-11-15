print("**********PROGRAMMED BY:**********")
print("*******Pauline Joy R. Mingo*******")

#Use dictionary to store the information, using full names as key and value is another dictionary of infos

#display menu
print()
print("==========M E N U==========")
print()
print("1 => Add an item")
print("2 => Search")
print("3 => Exit the program")
print()
print("===========================")
print()



while True:
    userInputFunct = int(input("What do you want to do: 1, 2 or 3? "))

#dictionary
    personaldatadict = {}

#diplay Option  1 (add an item)
    if userInputFunct == 1:

        print()
        print("Please enter the needed information below.") 
        print()
        name = input("Enter your full name: ")
        print()
        age = int(input("Enter your age: "))
        print()
        address = input("Enter your address: ")
        print()
        contact_num = int(input("Enter your contact number: "))
        print()
        vaccination_status = input("Enter your Vaccination status: ")
        print()
        print("Yay! Your informations have been saved!")
        print()


#display Option 2 (search for an item)
    elif userInputFunct == 2:

    #assigning keys and their corresponding values in the dictionary
        personaldatadict["Full Name"] = name
        personaldatadict["Age"] = age
        personaldatadict["Address"] = address
        personaldatadict["Contact Number"] = contact_num
        personaldatadict["Vaccination Status"] = vaccination_status
       

    #user input for the viewing of record
        full_name = input("Enter your full name: ")
        print()
        print("Search result for: ", full_name)
        print()
        
    #nested if-else statement to compare if the entered information is exisiting 
        if full_name in name:
            for key in personaldatadict:
                print(key, ":", personaldatadict[key])
                print()
        else: 
            print("The data is not existing. Please try again.")
            print()
#display Option 3 (exit the program) 
    elif userInputFunct == 3: 
        exitVerification = input("Are you sure you want to exit the program? (Yes or No) ")
        if exitVerification == "Yes":
            print ("THANK YOU FOR USING THIS PROGRAM!")
            break
        else:
            continue






