print("**********PROGRAMMED BY:**********")
print("*******Pauline Joy R. Mingo*******")

#Use dictionary to store the information, using full names as key and value is another dictionary of infos

#display menu
def menu():
    print()
    print("==========M E N U==========")
    print()
    print("1 => Add an item")
    print("2 => Search")
    print("3 => Exit (y/n)")
    print()
    print("===========================")
    print()


menu()
PersonalInfoDict = {
    "Full name": " ", 
    "Age": " ", 
    "Current Address": " ", 
    "Contact Number": " ", 
    "Vaccination Status": " ",

}


while True:
    options = int(input("What do you want to do: 1, 2 or 3? "))

#Allow users to select and add item in the menu (check if valid)
    if options == 1:
        print("You must add an item")


        print()
        name = input("Full Name: ")
        PersonalInfoDict["Full Name"] = name

        print()
        age = input("Age:  ")
        PersonalInfoDict["Age"] = age

        print()
        current_address = input("Current Address: ")
        PersonalInfoDict["Current Address: "] = current_address

        print()
        contact_number = input("Contact Number: ")
        PersonalInfoDict["Contact Number"] = contact_number

        print()
        vaccination_status = input("Vaccination Status: ")
        PersonalInfoDict["Vaccination Status: "] = vaccination_status

        print()
        print("Yay! Your personal information is saved and recorded!")
        print()


#Perform the selected options (search for an information)
    elif options == 2:
        print("You wish to search for an item")
        








