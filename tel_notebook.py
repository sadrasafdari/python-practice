tel_notebook = []
try:
    with open("contacts.txt", "r") as file:
        tel_notebook = file.read().splitlines()
except FileNotFoundError:
    pass

def save_contacts():
    with open("contacts.txt", "w") as file:
        for contact in tel_notebook:
            file.write(contact + "\n")

while True:
    print("\nTelList")
    print("1. View TelList")
    print("2. Add to TelList")
    print("3. Remove")
    print("4. Search in list")
    print("5. Exit")
    choice = input("Enter number of your act: ")

    if choice == "2":
        contact = input("Add contact (Name - Phone): ")
        tel_notebook.append(contact)

        save_contacts()

    elif choice == "1":
        if len(tel_notebook) == 0:
            print("No contacts")

        else:
            for contact in tel_notebook:
                print(contact)

    elif choice == "3":
        contact = input("Enter contact to remove: ")

        if contact in tel_notebook:
            tel_notebook.remove(contact)

            save_contacts()
            print("removed")
        else:
            print("not found")

    elif choice == "4":
        search = input("Your search: ")
        found = False

        for contact in tel_notebook:
            if search.lower() in contact.lower():
                print(contact)
                found = True

        if not found:
            print("No found")

    elif choice == "5":
        print("goodluck")
        break

    else:
        print("Error")