contacts = {}
while True:
    print("\n--CONTACTS--")
    print("1. Add a contact(name , phone)")
    print("2. View all contacts")
    print("3. Search for a contact by name")
    print("4. Quit")
    
    choice = input("Please choose a number from 1 to 4:")
    if choice == "1":
        name = input("Enter the name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact saved!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet.")
        else:
            print("\nYour contacts:")
            for name, phone in contacts.items():
                print(name, "-", phone)
    elif choice == "3":
        name = input("Enter a name to search: ")

        if name in contacts:
            print(name, "-", contacts[name])
        else:
            print("Contacts not found.")
    elif choice == "4":
        print("Goodbye!Please visit again.")
        break
    else:
        print("Please choose from 1 to 4")

