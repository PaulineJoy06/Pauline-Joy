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
    contact = {}

    #diplay first option (add an item/s)
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

    #display second option (search existing item/s)
    elif userInputFunct == 2:

        #assigning keys and their corresponding values in the dictionary
        contact["Full Name"] = name
        contact["Age"] = age
        contact["Address"] = address
        contact["Contact Number"] = contact_num
        contact["Vaccination Status"] = vaccination_status
       

        #user input for the viewing of record
        full_name = input("Enter your full name: ")
        print("Search result for: ", full_name)
        print()
        
        #nested if-else statement to compare if the entered data is exisiting 
        if full_name in name:
            for key in contact:
                print(key, ":", contact[key])
                print()
        else: 
            print("The data is not existing in the existing, check the entered input if correct")
            print()






